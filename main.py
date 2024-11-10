from fastapi import FastAPI
from app.main import api_router
import logging
from app.db.database import init_db
from contextlib import asynccontextmanager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(api_router)


@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.info("Inicializando la base de datos y cargando datos si es necesario...")
    init_db()
    logger.info("Inicialización completa.")

    yield
    logger.info("Aplicación cerrándose.")


app.router.lifespan_context = lifespan
