from contextlib import asynccontextmanager

from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from PIL import Image
from io import BytesIO

from moin_moin.backend.ml import SimilarityModel

ML_MODEL = {}

institutions = {
    "Police Department": "The police deals with crime and violence related topics.",
    "Fire Department": "The fire department deals with fire and other emergency situations.",
    "Hospital": "The hospital deals with health and medical related topics.",
    "Garbage Disposal": "The garbage disposal deals with waste and recycling related topics.",
    "Construction Department": "The construction department deals with building and infrastructure related topics.",
}

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    ML_MODEL["similarity_model"] = SimilarityModel("clip-ViT-B-32").set_text_embedding(institutions)
    yield
    # Clean up the ML models and release the resources
    ML_MODEL.clear()



app = FastAPI(lifespan=lifespan)

def _predict(img_array: Image):
    """This function decoupled from the API exists for debugging purposes."""
    return ML_MODEL["similarity_model"].find_similarity(img_array)


@app.get("/")
def root():
    """Root endpoint."""
    return {"message": "Health"}


@app.post("/predict")
async def predict(height: int = Form(...) , width:int=Form(...), file: UploadFile = File(...)):
    
    file_bytes = await file.read()
    buffer = BytesIO(file_bytes)
    image = Image.open(buffer)
    prediction = _predict(image)
        
    return JSONResponse(content={"prediction": prediction}, status_code=200)
