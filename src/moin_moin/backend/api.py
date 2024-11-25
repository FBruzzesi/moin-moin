"""Module that builds FastAPI application with endpoints to save, predict and gather data."""

from __future__ import annotations

from contextlib import asynccontextmanager
from io import BytesIO
from typing import TYPE_CHECKING
from typing import Annotated
from typing import Final

from fastapi import Depends
from fastapi import FastAPI
from fastapi import File
from fastapi import Form
from fastapi import UploadFile
from PIL import Image
from sqlmodel import Session
from sqlmodel import SQLModel
from sqlmodel import create_engine
from sqlmodel import select

from moin_moin.backend._db import Prediction
from moin_moin.backend._db import PublicRecord
from moin_moin.backend._db import UserUploadData
from moin_moin.backend._institutions import INSTITUTIONS
from moin_moin.backend._ml import ClipModel

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator
    from collections.abc import Generator

    from sqlmodel import Engine


ML_MODEL: dict[str, ClipModel] = {}

DB_NAME: Final[str] = "sqlite:///db/moin-moin.db"
ENGINE: Final[Engine] = create_engine(DB_NAME)


def get_session() -> Generator[Session, None, None]:
    """Yield SQLModel session."""
    with Session(ENGINE) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:  # noqa: ARG001
    """FastAPI Lifespan: loads and instantiate the model at startup, delete at shutdown."""
    SQLModel.metadata.create_all(ENGINE)
    ML_MODEL["similarity_model"] = ClipModel(text_options=INSTITUTIONS)

    yield

    ML_MODEL.clear()


app = FastAPI(lifespan=lifespan)


@app.get("/")
def root() -> dict[str, str]:
    """Root endpoint."""
    return {"message": "Health"}


@app.post("/save")
async def save(  # noqa: PLR0913
    session: SessionDep,
    latitude: Annotated[float, Form()],
    longitude: Annotated[float, Form()],
    notes: Annotated[str, Form()],
    tags: Annotated[str, Form()],
    image_bytes: Annotated[UploadFile, File()],
) -> dict[str, int | None]:
    """Save the input data into database records into user upload data table."""
    image_bytes = await image_bytes.read()
    record = UserUploadData(
        image=image_bytes,  # type: ignore[assignment]
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
    session: SessionDep,
    record_id: Annotated[int, Form()],
    notes: Annotated[str, Form()],
    file: Annotated[UploadFile, File(...)],
) -> dict[str, str]:
    """Predict image category via ML model."""
    file_bytes = await file.read()
    buffer = BytesIO(file_bytes)
    image = Image.open(buffer)
    prediction = ML_MODEL["similarity_model"].predict(image, notes)

    pred_record = Prediction(record_id=record_id, prediction=prediction)

    session.add(pred_record)
    session.commit()

    return {"prediction": prediction}


@app.get("/load-records", response_model=list[PublicRecord])
async def load_records(session: SessionDep) -> list[PublicRecord]:
    """Load all the records with their predictions, ignores associated image."""
    statement = select(
        UserUploadData.latitude,
        UserUploadData.longitude,
        UserUploadData.notes,
        UserUploadData.tags,
        Prediction.prediction,
    ).join(Prediction)
    records = session.exec(statement).all()
    return [PublicRecord(**row._mapping) for row in records]  # noqa: SLF001
