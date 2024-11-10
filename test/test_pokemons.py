from fastapi.testclient import TestClient
from app.routers.pokemons import POKEMON_DATA
from app.models.pokemon import Pokemon
from app.models.naturaleza import Naturaleza
from main import app
from test.jsons import nature_1, nature_2, nature_3, infernape_mock, movimientos_infernape
import pytest

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


def test_get_pokemon_movimientos_encontrado():
    response = client.get("/pokemons/392/moves")
    assert response.status_code == 200
    assert response.json() == movimientos_infernape


def test_get_pokemon_movimientos_no_encontrado():
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
