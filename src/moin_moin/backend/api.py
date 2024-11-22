import numpy as np

from moin_moin.backend.ml import SimilarityModel

institutions = {
    "Police Department": "The police deals with crime and violence related topics.",
    "Fire Department": "The fire department deals with fire and other emergency situations.",
    "Hospital": "The hospital deals with health and medical related topics.",
    "Garbage Disposal": "The garbage disposal deals with waste and recycling related topics.",
    "Construction Department": "The construction department deals with building and infrastructure related topics.",
}

model = SimilarityModel("clip-ViT-B-32")
model.set_text_embedding(institutions)


def get_institution(img_array: np.array):
    return model.find_similarity(img_array)
