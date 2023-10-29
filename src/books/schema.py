from datetime import datetime, timezone
from functools import partial

from pydantic import BaseModel, Field


class BookSchema(BaseModel):
    unique_id: int
    title: str
    author: str | None = Field(default=None)


class AddBookRequestSchema(BaseModel):
    title: str
    author: str | None = Field(default=None)


class UpdateBookRequestSchema(BaseModel):
    title: str | None = Field(default=None)
    author: str | None = Field(default=None)


class BookResponseSchema(BaseModel):
    unique_id: int
    datetime: str = Field(default_factory=partial(datetime.now, tz=timezone.utc))

    class Config:
        json_encoders = {datetime: lambda dt: dt.isoformat()}
