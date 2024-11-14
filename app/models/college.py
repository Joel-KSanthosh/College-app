from enum import Enum

from sqlmodel import SQLModel, Field


class Batch(Enum):
    ug = 'UG'
    pg = 'PG'


class CourseBase(SQLModel):
    name: str
    duration: int = Field(default=4)
    type: Batch


class Course(CourseBase):

    __tablename__ = 'course'

    id: int | None = Field(default=None, primary_key=True)




