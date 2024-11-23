from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Self

from sentence_transformers import SentenceTransformer

if TYPE_CHECKING:
    from PIL import Image


class ClipModel:
    """Wrapper of SentenceTransformer, clip-ViT-B-32 model.

    Process is to store embeddings of categories we can match images with, and then at
    prediction time to return the category closest to the given image.
    """

    def __init__(self: Self, text_options: dict[str, str]) -> None:
        self.model = SentenceTransformer("clip-ViT-B-32")
        self.model.eval()
        self.labels = list(text_options.keys())
        self.text_embedding = self.model.encode(list(text_options.values()))

    def predict(self: Self, image: Image) -> str:
        """Embed the image and return the closest text embedding."""
        img_emb = self.model.encode(image)
        similarity_array = self.model.similarity(img_emb, self.text_embedding)
        return self.labels[similarity_array.argmax().item()]
