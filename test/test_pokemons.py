import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def client() -> TestClient:
    return TestClient(app)

def test_get_pokemon(client):
    infernape_mock = {
        "id": 392,
        "nombre": "infernape",
        "imagen": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/392.png",
        "tipos": ["Fuego", "Lucha"],
        "habilidades": ["Mar Llamas", "Puño Férreo"],
        "altura": 12,
        "peso": 550,
        "estadisticas": {
            "hp": 76,
            "attack": 104,
            "defense": 71,
            "special-attack": 104,
            "special-defense": 71,
            "speed": 108,
            "accuracy": 100,
            "evasion": 100
        }
    }

    response = client.get("/pokemons/392")

    assert response.status_code == 200
    assert response.json() == infernape_mock
