from fastapi.testclient import TestClient

from main import app
from app.routers.pokemons import pokemons

client = TestClient(app)
def test_get_pokemons():
    respuesta = client.get("/pokemon/")
    contenido = respuesta.json()
    assert respuesta.status_code == 200
