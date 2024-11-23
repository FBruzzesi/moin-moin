from sentence_transformers import SentenceTransformer


class ClipModel:
    def __init__(self, **kwargs):
        self.model = SentenceTransformer("clip-ViT-B-32")
        text_options = kwargs["text_options"]
        self.labels = list(text_options.keys())
        self.text_embedding = self.model.encode(list(text_options.values()))

    def predict(self, text_or_image):
        # text has to be predefined e.g. police, fire department, etc
        img_emb = self.model.encode(text_or_image)
        similarity_array = self.model.similarity(img_emb, self.text_embedding)
        return self.labels[similarity_array.argmax().item()]
