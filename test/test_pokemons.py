from fastapi.testclient import TestClient
from app.routers.pokemons import POKEMON_DATA
from app.models.pokemon import Pokemon
from app.models.movimiento import Movimiento
from app.models.pokemonMovimiento import PokemonMovimiento
from main import app
from sqlmodel import Session
from test.jsons import nature_1, nature_2, nature_3, infernape_mock, movimientos_infernape, relaciones_infernape, infernape_nuevo_modelo


client = TestClient(app)


def test_get_pokemons():
    respuesta = client.get("/pokemons/")
    contenido = respuesta.json()
    assert respuesta.status_code == 200
    assert contenido[0]["id"] == 1


def test_get_pokemon_encontrado(client):
    response = client.get("/pokemons/392")
    assert response.status_code == 200
    assert response.json() == infernape_mock


def test_get_pokemon_no_encontrado(client):
    response = client.get("/pokemons/0")  # ID 0 no existe.
    assert response.status_code == 404
    assert response.json() == {"detail": "Pokémon no encontrado."}


def test_get_pokemon_movimientos_encontrado(session: Session, client: TestClient):
    pokemon = Pokemon(**infernape_nuevo_modelo)
    movimientos = [Movimiento(**data) for data in movimientos_infernape]
    pokemon_movimientos = [PokemonMovimiento(**data) for data in relaciones_infernape]
    
    session.add(pokemon)
    session.add_all(movimientos)
    session.add_all(pokemon_movimientos)
    session.commit()
    response = client.get("/pokemons/392/moves")
    content = response.json()
    assert response.status_code == 200
    assert sorted(content, key=lambda x: x['id']) == sorted(movimientos_infernape, key=lambda x: x['id']) #ordena las listas, para poder ser comparadas


def test_get_pokemon_movimientos_no_encontrado(session: Session, client: TestClient):
    response = client.get("/pokemons/0/moves")  # ID 0 no existe
    assert response.status_code == 404
    assert response.json() == {"detail": "Pokémon no encontrado."}


def test_borrar_un_pokemon():
    POKEMON_DATA.clear()
    POKEMON_DATA.append(infernape_mock)
    response = client.delete("pokemons/392")
    assert response.status_code == 200


def test_borrar_pokemon_no_existe():
    POKEMON_DATA.clear()
    response = client.delete("/pokemons/10")
    assert response.status_code == 404
    assert response.json()["detail"] == "No se encontro ese id en nuestros pokemons"


def test_crear_pokemon():
    POKEMON_DATA.clear()
    response = client.post("/pokemons", json=infernape_mock)
    assert response.status_code == 201
    assert response.json() == infernape_mock


def test_crear_pokemon_con_id_existente():
    POKEMON_DATA.clear()
    POKEMON_DATA.append(infernape_mock)
    response = client.post("/pokemons", json=infernape_mock)

    assert response.status_code == 400
    assert response.json()["detail"] == "Ya existe un pokemon con ese id"
