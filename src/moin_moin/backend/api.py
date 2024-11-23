from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import FastAPI, File, UploadFile, Form, Depends
from PIL import Image
from io import BytesIO
from sqlmodel import Session, select
from moin_moin.backend.ml import ClipModel
from moin_moin.backend.db import Record, Prediction, engine, PublicRecord


ML_MODEL = {}


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

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
    ML_MODEL["similarity_model"] = ClipModel().fit(institutions)
    yield
    # Clean up the ML models and release the resources
    ML_MODEL.clear()


app = FastAPI(lifespan=lifespan)


def _predict(img_array: Image):
    """This function decoupled from the API exists for debugging purposes."""
    return ML_MODEL["similarity_model"].predict(img_array)


@app.get("/")
def root():
    """Root endpoint."""
    return {"message": "Health"}


@app.post("/save")
async def save(
    session: SessionDep,
    latitude: float = Form(...),
    longitude: float = Form(...),
    notes: str = Form(...),
    tags: str = Form(...),
    image_bytes: UploadFile = File(...),
):
    image_bytes = await image_bytes.read()
    record = Record(
        image=image_bytes,
        latitude=latitude,
        longitude=longitude,
        notes=notes,
        tags=tags,
    )

    session.add(record)
    session.commit()
    record_id = record.id

    return {"record-id": record_id}


@app.post("/predict")
async def predict(
    session: SessionDep, record_id: int = Form(), file: UploadFile = File(...)
):
    file_bytes = await file.read()
    buffer = BytesIO(file_bytes)
    image = Image.open(buffer)
    prediction = _predict(image)

    pred_record = Prediction(record_id=record_id, prediction=prediction)

    session.add(pred_record)
    session.commit()

    return {"prediction": prediction}


@app.get("/load-records", response_model=list[PublicRecord])
async def load_records(session: SessionDep):
    statement = select(
        Record.latitude,
        Record.longitude,
        Record.notes,
        Record.tags,
        Prediction.prediction,
    )  # .join(Prediction)
    records = session.exec(statement).all()
    return [PublicRecord(**row._mapping) for row in records]
