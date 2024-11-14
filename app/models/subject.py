from sqlmodel import SQLModel, Field


class Subject(SQLModel, table=True):

    __tablename__ = 'subject'

    id: int = Field(default=None, primary_key=True)
    name: str
    course_id: int = Field(foreign_key=True)
