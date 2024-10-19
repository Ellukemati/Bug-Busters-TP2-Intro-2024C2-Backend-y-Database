from fastapi.testclient import TestClient
from models import Pokemon, Naturaleza
from main import app
from app.routers.pokemons import Naturalezas, estadisticas, pokemons
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
