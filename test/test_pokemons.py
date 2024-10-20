from fastapi.testclient import TestClient
from app.routers.pokemons import pokemons
from models import Pokemon
from main import app
import pytest


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
            "evasion": 0,
        },
        "cadena_evolutiva": [390, 391, 392],
    }
    response = client.get("/pokemons/392")

    assert response.status_code == 200
    assert response.json() == infernape_mock


def test_get_pokemon_no_encontrado(client):
    response = client.get("/pokemons/0")  # ID 0 no existe.

    assert response.status_code == 404
    assert response.json() == {"detail": "Pokémon no encontrado."}


def test_borrar_un_pokemon():
    pokemon_existente = {
        "pokemon_id": 392,
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
            "evasion": 100,
        },
        "cadena_evolutiva": [390, 391, 392],
    }

    pokemons.append(pokemon_existente)
    response = client.delete("pokemons/392")

    assert response.status_code == 200


def test_borrar_pokemon_no_existe():
    response = client.delete("/pokemons/10")
    assert response.status_code == 404
    assert response.json()["detail"] == "No se encontro ese id en nuestros pokemons"


def test_crear_pokemon():
    nuevo_pokemon = {
        "pokemon_id": 392,
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
            "evasion": 100,
        },
        "cadena_evolutiva": [390, 391, 392],
    }
    response = client.post("/pokemons", json=nuevo_pokemon)

    assert response.status_code == 201
    assert response.json() == nuevo_pokemon


def test_crear_pokemon_con_id_existente():
    pokemon_existente = {
        "pokemon_id": 392,
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
            "evasion": 100,
        },
        "cadena_evolutiva": [390, 391, 392],
    }
    pokemons.append(pokemon_existente)
    response = client.post("/pokemons", json=pokemon_existente)

    assert response.status_code == 400
    assert response.json()["detail"] == "Ya existe un pokemon con ese id"
