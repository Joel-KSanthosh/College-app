from contextlib import asynccontextmanager
from typing import Annotated

import uvicorn
from fastapi import FastAPI
from fastapi.params import Depends
from sqlmodel import create_engine, Session, SQLModel
from app.config.settings import db_uri

__engine = create_engine(db_uri(), echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(__engine)
    print("SUCCESS")


@asynccontextmanager
async def lifespan(app: FastAPI): # noqa
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)


def get_session():
    with Session(__engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
