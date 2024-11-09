from test.jsons import (
    equipo_con_6_pokemons,
    equipo_mismo_id,
    equipo_siete_pokemons,
    equipo,
    nature_1,
    nature_2,
    nature_3,
)
from fastapi.testclient import TestClient
from app.models.equipos import EquipoPublic, Equipo, Integrante_pokemon, Integrante_pokemonPublic
from app.models.movimiento import Movimiento
from main import app
from app.models.naturaleza import Naturaleza
from sqlmodel import Session, select

from app.db.database import SessionDep

client = TestClient(app)


def test_get_natures():
    Naturalezas.clear()
    Naturalezas.append(nature_1)
    Naturalezas.append(nature_2)
    Naturalezas.append(nature_3)

    response = client.get("teams/natures")

    response = client.get("teams/natures")


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


def test_crear_equipo(session: SessionDep, client: TestClient):
    #Equipo(nombre="nombre",)
    response = client.post("/teams/", json=equipo_con_6_pokemons)
    assert response.status_code == 201
    content = response.json()
    assert content[0]["nombre"] == "Equipo Elite"
    assert content[0]["id_equipo"] == 12

def test_crear_equipo_mismo_id():
    teams.append(equipo_con_6_pokemons)
    response = client.post("/teams", json=equipo_mismo_id)
    assert response.status_code == 400
    assert response.json()["detail"] == "Ya existe un equipo con ese id"
    teams.clear()


def test_borrar_equipo_existente():

    teams.append(equipo)
    response = client.delete("teams/2")

    assert response.status_code == 200
    assert response.json() == equipo
    teams.clear()


def test_borrar_equipo_no_existe():

    response = client.delete("/teams/99")
    assert response.status_code == 404
    assert response.json()["detail"] == "No se encontro un equipo con ese id"


def test_get_teams():
    lista_vacia: list[Equipo] = []
    respuesta = client.get("/teams/")
    contenido = respuesta.json()
    assert respuesta.status_code == 200
    assert contenido == lista_vacia


def test_buscar_team_por_id():
    teams.append(equipo_con_6_pokemons)
    response = client.get("/teams/1")
    assert response.status_code == 200


def test_buscar_equipo_no_existente():
    response = client.get("/teams/100")
    assert response.status_code == 404
    assert response.json()["detail"] == "No se encontro el equipo"


def test_actualizar_equipo_existente():
    teams.append(equipo_con_6_pokemons)
    response = client.put("/teams", json=equipo_mismo_id)
    content = response.json()
    assert response.status_code == 200
    assert content["id_equipo"] == equipo_mismo_id["id_equipo"]
    assert content["nombre"] == equipo_mismo_id["nombre"]
    teams.clear()


def test_actualizar_equipo_no_existente():
    response = client.put("/teams", json=equipo)
    assert response.status_code == 404
    assert response.json()["detail"] == "No se encontro un equipo con ese id"

