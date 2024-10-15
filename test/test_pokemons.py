import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def client() -> TestClient:
    return TestClient(app)

def test_get_pokemon_encontrado(client):
    infernape_mock = {
        "pokemon_id": 392,
        "nombre": "infernape",
        "imagen": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/392.png",
        "tipos": ["Lucha", "Fuego"],
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
            "accuracy": 0,
            "evasion": 0
        },
        "cadena_evolutiva": [390, 391, 392]
    }

    response = client.get("/pokemons/392")

    assert response.status_code == 200
    assert response.json() == infernape_mock

def test_get_pokemon_no_encontrado(client):
    response = client.get("/pokemons/0") # ID 0 no existe.

    assert response.status_code == 404
    assert response.json() == {"detail": "Pokémon no encontrado."}
