from fastapi.testclient import TestClient
from app.routers.pokemons import POKEMON_DATA
from app.models.pokemon import Pokemon
from main import app
from jsons import (
    infernape_mock,
    movimientos_infernape,
    infernape_mock_post,
    infernape_mock_id1,
)
import pytest
from sqlmodel import Session
from app.db.database import SessionDep

client = TestClient(app)

# def test_get_pokemons():
#     respuesta = client.get("/pokemons/")
#     contenido = respuesta.json()
#     assert respuesta.status_code == 200
#     assert contenido[0]["id"] == 1


def test_get_pokemon_encontrado(session: Session, client: TestClient):
    session.add(infernape_mock)
    response = client.get("/pokemons/392")
    assert response.status_code == 200
    assert response.json() == infernape_mock.model_dump()


def test_get_pokemon_no_encontrado(session: Session, client: TestClient):
    response = client.get("/pokemons/0")  # ID 0 no existe.
    assert response.status_code == 404


# def test_get_pokemon_movimientos_encontrado():
#     response = client.get("/pokemons/392/moves")
#     assert response.status_code == 200
#     assert response.json() == movimientos_infernape


# def test_get_pokemon_movimientos_no_encontrado():
#     response = client.get("/pokemons/0/moves")  # ID 0 no existe
#     assert response.status_code == 404
#     assert response.json() == {"detail": "Pokémon no encontrado."}


def test_borrar_un_pokemon(session: Session, client: TestClient):
    session.add(infernape_mock_id1)
    session.commit()
    response = client.delete("/pokemons/1")
    assert response.status_code == 200
    assert response.json() == infernape_mock_id1.model_dump()


def test_borrar_pokemon_no_existe(session: Session, client: TestClient):
    response = client.delete("/pokemons/392")
    assert response.status_code == 404
    assert response.json()["detail"] == "No se encontro ese id en nuestros pokemons"


def test_crear_pokemon(session: Session, client: TestClient):
    response = client.post("/pokemons/", json=infernape_mock_post.model_dump())
    assert response.status_code == 201
