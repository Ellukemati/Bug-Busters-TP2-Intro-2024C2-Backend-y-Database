from fastapi.testclient import TestClient
from app.models.naturaleza import Naturaleza
from main import app
from test.jsons import infernape_mock, movimientos_infernape
import pytest
from sqlmodel import Session
from app.models.pokemon import Pokemon
from app.db.database import SessionDep
from app.models.movimiento import Movimiento
from app.models.pokemonMovimiento import PokemonMovimiento

from test.jsons import (
    greninja_mock,
    greninja_mockid1,
    infernape_mock,
    movimientos_infernape,
    relaciones_infernape,
    infernape_mock_post,
    infernape_mock_id1,
    infernape_json,
)

client = TestClient(app)


def test_get_pokemon_encontrados(session: Session, client: TestClient):
    # Hago un mock más para probarlo con 2

    session.add_all([infernape_mock, greninja_mock])
    session.commit()

    response = client.get("/pokemons")
    assert response.status_code == 200

    # Chequeo que los datos devueltos sean de todos los Pokémon cargados
    content = response.json()
    assert len(content) == 2
    assert content[0]["nombre"] == "infernape"
    assert content[1]["nombre"] == "greninja"


def test_get_pokemon_no_encontrados(session: Session, client: TestClient):
    response = client.get("/pokemons")  # No hay Pokémon en el mock de la db.

    assert response.status_code == 404
    assert response.json() == {
        "detail": "No se encontraron Pokémon en la base de datos."
    }


def test_get_pokemon_encontrado(session: Session, client: TestClient):
    session.add(greninja_mockid1)
    response = client.get("/pokemons/1")
    assert response.status_code == 200
    assert response.json() == greninja_mockid1.model_dump()


def test_get_pokemon_no_encontrado(session: Session, client: TestClient):
    response = client.get("/pokemons/0")  # ID 0 no existe.
    assert response.status_code == 404


def test_get_pokemon_movimientos_encontrado(session: Session, client: TestClient):
    pokemon = Pokemon(**infernape_json)
    movimientos = [Movimiento(**data) for data in movimientos_infernape]
    pokemon_movimientos = [PokemonMovimiento(**data) for data in relaciones_infernape]

    session.add(pokemon)
    session.add_all(movimientos)
    session.add_all(pokemon_movimientos)
    session.commit()
    response = client.get("/pokemons/392/moves")
    content = response.json()
    assert response.status_code == 200
    assert sorted(content, key=lambda x: x["id"]) == sorted(
        movimientos_infernape, key=lambda x: x["id"]
    )  # ordena las listas, para poder ser comparadas


def test_get_pokemon_movimientos_no_encontrado(session: Session, client: TestClient):
    response = client.get("/pokemons/0/moves")  # ID 0 no existe
    assert response.status_code == 404
    assert response.json() == {"detail": "Pokémon no encontrado."}


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
