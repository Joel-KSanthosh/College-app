from datetime import datetime
from enum import Enum

from pydantic import EmailStr
from sqlmodel import SQLModel, Field


class Roles(Enum):
    admin = "ADMIN"
    student = "STUDENT"
    faculty = "FACULTY"
    associate = "ASSOCIATE"


class UserBase(SQLModel):
    name: str
    email: EmailStr = Field(index=True)
    age: int


class User(UserBase, table=True):

    __tablename__ = 'user'

    id: int | None = Field(default=None, primary_key=True)
    password: str
    role: Enum
    created_at: datetime = Field(default=datetime.now(), allow_mutation=False)
    updated_at: datetime = Field(default=datetime.now())






