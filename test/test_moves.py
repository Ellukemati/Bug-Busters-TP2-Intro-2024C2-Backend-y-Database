# incluyan clases de lo que haga falta
from fastapi import APIRouter#,  HTTPException, status
from main import app

from fastapi.testclient import TestClient
client = TestClient(app)
from app.models.movimiento import Movimiento








