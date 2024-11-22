from sentence_transformers import SentenceTransformer


class SimilarityModel:
    def __init__(self, model_name):
        self.model = SentenceTransformer(model_name)

    def set_text_embedding(self, text_options: dict):
        self.labels = list(text_options.keys())
        self.text_embedding = self.encode_text(list(text_options.values()))
        return self

    def encode_image(self, image):
        return self.model.encode(image)

    def encode_text(self, text):
        return self.model.encode(text)

    def find_similarity(self, image):
        # text has to be predefined e.g. police, fire department, etc
        img_emb = self.encode_image(image)
        similarity_array = self.model.similarity(img_emb, self.text_embedding)
        return self.labels[similarity_array.argmax().item()]
