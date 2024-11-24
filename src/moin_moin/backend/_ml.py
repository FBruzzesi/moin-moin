from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Self

import torch
from sentence_transformers import SentenceTransformer

if TYPE_CHECKING:
    from PIL import Image


class ClipModel:
    """Wrapper of SentenceTransformer, clip-ViT-B-32 model.

    Process is to store embeddings of categories we can match images with, and then at
    prediction time to return the category closest to the given image.
    """

    def __init__(self: Self, text_options: dict[str, str]) -> None:
        self.model = SentenceTransformer("clip-ViT-B-32", cache_folder="models")
        self.model.eval()
        self.labels = list(text_options.keys())
        self.text_embedding = self.model.encode(list(text_options.values()))

    def predict(self: Self, image: Image, description: str) -> str:
        """Embed the image and return the closest text embedding."""
        img_emb = self.model.encode(image)
        description_emb = self.model.encode(description)

        similarity_array_image = self.model.similarity(img_emb, self.text_embedding)
        similarity_array_description = torch.zeros(similarity_array_image.shape)
        if description != "":
            similarity_array_description = self.model.similarity(description_emb, self.text_embedding)

        combined_similarity = similarity_array_image + similarity_array_description
        return self.labels[combined_similarity.argmax().item()]
