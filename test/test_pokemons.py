from fastapi.testclient import TestClient
from models import Pokemon
from main import app
from app.routers.pokemons import pokemons


client = TestClient(app)


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
    }
    pokemons.append(pokemon_existente)
    response = client.delete("pokemons/392")

    assert response.status_code == 200


def test_borrar_pokemon_no_existe():
    response = client.delete("/pokemons/10")
    assert response.status_code == 404
    assert response.json()["detail"] == "No se encontro ese id en nuestros pokemons"
