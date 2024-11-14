from enum import Enum

from sqlmodel import SQLModel, Field


class Batch(Enum):
    ug = 'UG'
    pg = 'PG'


class CourseBase(SQLModel, table=True):

    __tablename__ = 'course'

    id: int | None = Field(default=None, primary_key=True)
    name: str
    duration: int = Field(default=4)
    type: Batch
    dept_id: Field(foreign_key='department.id')

# class Course(CourseBase):
#
#     __tablename__ = 'course'
#
#     id: int | None = Field(default=None, primary_key=True)
