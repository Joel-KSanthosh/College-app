from sqlmodel import SQLModel, Field


class Semester(SQLModel, table=True):

    __tablename__ = 'semester'

    id: int | None = Field(default=None, primary_key=True)
    name: str
    course_id: int = Field(foreign_key='course.id')
