from typing import Optional

from sqlmodel import Field, SQLModel, create_engine

DB_NAME = "sqlite:///moin-moin.db"


class Record(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    image: bytes
    latitude: float
    longitude: float
    notes: str
    tags: str


class Prediction(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    record_id: Optional[int] = Field(default=None, foreign_key="record.id")
    prediction: str


class PublicRecord(SQLModel):
    latitude: float
    longitude: float
    notes: str
    tags: str
    prediction: str


engine = create_engine(DB_NAME)
SQLModel.metadata.create_all(engine)
