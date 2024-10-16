# incluyan clases de lo que haga falta
from fastapi import APIRouter#,  HTTPException, status
from main import app
from fastapi.testclient import TestClient
client = TestClient(app)










def test_get_moves_id_pokemon():
    respuesta = client.get("/pokemon/3")
    contenido = respuesta.json()
    assert respuesta.status_code == 200
    assert len(contenido) == 3