from fastapi import FastAPI
from app.main import api_router
import logging
from app.db.database import init_db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(api_router)


@app.on_event("startup")
def startup_event():
    logger.info("Inicializando la base de datos y cargando datos si es necesario...")
    init_db()
    logger.info("Inicialización completa.")
