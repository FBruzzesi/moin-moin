from __future__ import annotations

from datetime import UTC
from datetime import datetime

from sqlmodel import Field
from sqlmodel import SQLModel


class UserUploadData(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    image: bytes
    latitude: float
    longitude: float
    notes: str
    timestamp: datetime = Field(default=datetime.now(tz=UTC))


class Prediction(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    record_id: int | None = Field(default=None, foreign_key="useruploaddata.id")
    prediction: str


class PublicRecord(SQLModel):
    latitude: float
    longitude: float
    notes: str
    prediction: str
    timestamp: datetime
