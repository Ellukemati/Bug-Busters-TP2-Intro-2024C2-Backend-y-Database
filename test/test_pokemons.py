from fastapi.testclient import TestClient
from models import Pokemon, Naturaleza
from main import app
from app.routers.pokemons import Naturalezas, estadisticas, pokemons, POKEMON_DATA
from test.jsons import nature_1, nature_2, nature_3, infernape_mock
import pytest

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

def test_get_pokemon_encontrado(client):

    response = client.get("/pokemons/392")

    assert response.status_code == 200
    assert response.json() == infernape_mock


def test_get_pokemon_no_encontrado(client):
    response = client.get("/pokemons/0")  # ID 0 no existe.

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
