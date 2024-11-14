from sqlmodel import SQLModel, Field


class Student(SQLModel, table=True):

    __tablename__ = 'student'

    id: int = Field(foreign_key='user.id', unique=True)
    roll_no: str = Field(primary_key=True)
