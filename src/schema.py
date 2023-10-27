from pydantic import BaseModel

class AddBookRequestSchema(BaseModel):
    title: str
    author: str