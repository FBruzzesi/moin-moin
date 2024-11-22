import torch
from sentence_transformers import SentenceTransformer
## from PIL import Image


class SimilarityModel:
    def __init__(self, model_name):
        self.model = SentenceTransformer(model_name)

    def set_text_embedding(self, text_options: dict):
        self.labels = text_options.keys()
        self.text_embedding = [self.encode_text(text) for text in text_options.values]

    def encode_image(self, img_array):  # shape??
        return self.model.encode(img_array)

    def encode_text(self, text):
        return self.model.encode(text)

    def find_similarity(self, img_array):  # text has to be predefined e.g. police, fire department, etc
        img_emb = self.encode_image(img_array)
        similarity_array = self.model.similarity(img_emb, self.text_embedding)
        return self.labels[torch.argmax(similarity_array).item()]
