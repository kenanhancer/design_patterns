# Pydantic Schemas
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    email: EmailStr


class User(UserBase):
    id: int
