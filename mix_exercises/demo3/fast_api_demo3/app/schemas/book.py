from pydantic import BaseModel


# Pydantic Schemas
class BookBase(BaseModel):
    title: str
    author: str


class Book(BookBase):
    id: int
