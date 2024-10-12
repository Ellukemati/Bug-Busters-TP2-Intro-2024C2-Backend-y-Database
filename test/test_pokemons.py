from fastapi.testclient import TestClient
from app.models import Pokemon
from app.main import app
from app.routers.pokemons import pokemons


client = TestClient(app)


def test_crear_pokemon():
    nuevo_pokemon = {
        "id": 10000,
        "nombre": "Pikachu",
        "imagen": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/10000.png",
        "tipo": "Electrico",
    }

    response = client.post("/pokemons/", json=nuevo_pokemon)

    assert response.status_code == 201
    assert response.json() == nuevo_pokemon


def test_crear_pokemon_con_id_existente():
    pokemon_existente = {
        "id": 10000,
        "nombre": "Pikachu",
        "imagen": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/10000.png",
        "tipo": "Electrico",
    }
    pokemons.append(pokemon_existente)

    response = client.post("/pokemons/", json=pokemon_existente)

    assert response.status_code == 400
    assert response.json()["detail"] == "Ya existe un pokemon con ese id"


def test_borrar_un_pokemon():
    pokemon_existente = {
        "id": 10000,
        "nombre": "Pikachu",
        "imagen": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/10000.png",
        "tipo": "Electrico",
    }
    pokemons.append(pokemon_existente)
    response = client.delete("pokemons/10000")

    assert response.status_code == 200
