from fastapi.testclient import TestClient
from models import Pokemon, Naturaleza
from main import app
from app.routers.pokemons import Naturalezas, estadisticas
from test.jsons import nature_1, nature_2, nature_3

client = TestClient(app)


def test_get_natures():
    Naturalezas.clear()
    Naturalezas.append(nature_1)
    Naturalezas.append(nature_2)
    Naturalezas.append(nature_3)
    response = client.get("/pokemons/natures")
    assert response.status_code == 200

    data = response.json()

    assert data[0]["nombre"] == "hardy"
    assert data[0]["aumenta_estadistica"] == "attack"
    assert data[0]["reduce_estadistica"] == "attack"

    assert data[1]["nombre"] == "bold"
    assert data[1]["aumenta_estadistica"] == "defense"
    assert data[1]["reduce_estadistica"] == "attack"

    assert data[2]["nombre"] == "modest"
    assert data[2]["aumenta_estadistica"] == "special-attack"
    assert data[2]["reduce_estadistica"] == "attack"
