from typing import Generator, Annotated
from sqlmodel import SQLModel, Session, create_engine, select
from fastapi import Depends

from app.models.naturaleza import Naturaleza
from app.db.cargar_naturalezas import cargar_naturalezas
from app.models.movimiento import Movimiento
from app.db.cargar_movimientos import cargar_movimientos
import logging

# Configura el logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


SQLITE_FILE_PATH = "app/db/database.db"

engine = create_engine(f"sqlite:///{SQLITE_FILE_PATH}")


def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_db)]


def init_db():
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:

        if not session.exec(select(Naturaleza)).first():
            logger.info("Cargando naturalezas...")
            cargar_naturalezas(session)
            logger.info("Naturalezas cargadas con exito.")
        if not session.exec(select(Movimiento)).first():
            logger.info("Cargando movimientos...")
            cargar_movimientos(session)
            logger.info("Movimientos cargados con exito.")
