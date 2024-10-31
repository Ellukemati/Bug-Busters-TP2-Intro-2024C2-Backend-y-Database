from typing import Generator, Annotated
from sqlmodel import SQLModel, Session, create_engine
from fastapi import Depends

SQLITE_FILE_PATH = "app/db/database.db"

engine = create_engine(f"sqlite:///{SQLITE_FILE_PATH}")

def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_db)]

def init_db():
    SQLModel.metadata.create_all(engine)