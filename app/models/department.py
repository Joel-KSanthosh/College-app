from sqlmodel import SQLModel, Field


class Department(SQLModel, table=True):

    __tablename__ = 'department'

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    active: bool = Field(default=True)
