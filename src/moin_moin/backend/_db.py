from __future__ import annotations

from sqlmodel import Field
from sqlmodel import SQLModel


class UserUploadData(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    image: bytes
    latitude: float
    longitude: float
    notes: str
    tags: str


class Prediction(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    record_id: int | None = Field(default=None, foreign_key="useruploaddata.id")
    prediction: str


class PublicRecord(SQLModel):
    latitude: float
    longitude: float
    notes: str
    tags: str
    prediction: str
