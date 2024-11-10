from main import app
from app.routers.pokemons import lista_contenido_limitado
from fastapi.testclient import TestClient
from app.models.movimiento import Movimiento
from test.jsons import movimiento_existente_id_190,movimiento_existente_id_46
from sqlmodel import Session

client = TestClient(app)


def test_get_moves_id_pokemon_3():
    respuesta = client.get("/moves/3/pokemon")
    contenido = respuesta.json()
    assert respuesta.status_code == 200
    assert contenido[0]["id"] == 35
    assert contenido[1]["nombre"] == "clefable"
    assert (
        contenido[0]["imagen"]
        == "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/35.png"
    )
    assert contenido[0]["tipos"][0] == "Hada"


def test_get_moves_id_pokemon_176():
    respuesta = client.get("/moves/176/pokemon")
    contenido = respuesta.json()
    assert respuesta.status_code == 200
    assert len(contenido) == 3
    assert contenido[0]["id"] == 137
    assert contenido[1]["id"] == 233
    assert contenido[2]["id"] == 474


def test_get_moves_id_pokemon_10001():
    respuesta = client.get("/moves/10001/pokemon")
    contenido = respuesta.json()
    assert respuesta.status_code == 200
    assert len(contenido) == 0


def test_get_moves_id_pokemon_vacio():
    respuesta = client.get("/moves/80000/pokemon")
    assert respuesta.status_code == 404


def test_get_moves_id_pokemon_vacio_2():
    respuesta = client.get("/moves/900/pokemon")
    assert respuesta.status_code == 404


def test_get_moves_id_pokemon_176():
    respuesta = client.get("/moves/25/pokemon")
    contenido = respuesta.json()
    assert respuesta.status_code == 200
    assert len(contenido) == 233


def test_obtener_movimiento_existente(session: Session, client: TestClient):
    movimiento = Movimiento(**movimiento_existente_id_190)
    session.add(movimiento)
    session.commit()
    response = client.get("moves/190")
    content = response.json()
    assert response.status_code == 200
    assert content == movimiento_existente_id_190


def test_obtener_movimento_no_existente(session: Session, client: TestClient):
    response = client.get("moves/850")
    assert response.status_code == 404


def test_obtener_movimiento_existente_con_casillas_vacias(session: Session, client: TestClient):
    movimiento = Movimiento(**movimiento_existente_id_46)
    session.add(movimiento)
    session.commit()

    response = client.get("moves/46")
    content = response.json()
    assert response.status_code == 200
    assert content == movimiento_existente_id_46
