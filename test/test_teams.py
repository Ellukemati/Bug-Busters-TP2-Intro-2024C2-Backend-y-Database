from test.jsons import (
    equipo_con_6_pokemons,
    equipo_mismo_id,
    equipo_siete_pokemons,
    equipo,
    naturaleza_1,
    naturaleza_2,
    naturaleza_3,
)
from fastapi.testclient import TestClient
from app.models.equipos import EquipoPublic, Equipo, Integrante_pokemon, Integrante_pokemonPublic
from app.models.movimiento import Movimiento
from main import app
from app.models.naturaleza import Naturaleza
from sqlmodel import Session, select
from app.db.database import SessionDep

client = TestClient(app)

def test_get_natures(session: Session, client: TestClient) -> None:


    session.add(naturaleza_1)
    session.add(naturaleza_2)
    session.add(naturaleza_3)
    session.commit()
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


# def test_crear_teams_seis_pokemons():
#     response = client.post("/teams", json=equipo_con_6_pokemons)
#     assert response.status_code == 201
#     data = response.json()

#     equipo_creado = data[0]
#     assert equipo_creado["id_equipo"] == equipo_con_6_pokemons["id_equipo"]
#     assert equipo_creado["nombre"] == equipo_con_6_pokemons["nombre"]
#     teams.clear()


# def test_crear_team_con_siete_pokemons():
#     response = client.post("/teams", json=equipo_siete_pokemons)
#     assert response.status_code == 400
#     assert response.json()["detail"] == "Puedes tener un maximo de seis pokemons"


# def test_crear_equipo_mismo_id():
#     teams.append(equipo_con_6_pokemons)
#     response = client.post("/teams", json=equipo_mismo_id)
#     assert response.status_code == 400
#     assert response.json()["detail"] == "Ya existe un equipo con ese id"
#     teams.clear()


# def test_borrar_equipo_existente():

#     teams.append(equipo)
#     response = client.delete("teams/2")

#     assert response.status_code == 200
#     assert response.json() == equipo
#     teams.clear()


# def test_borrar_equipo_no_existe():

#     response = client.delete("/teams/99")
#     assert response.status_code == 404
#     assert response.json()["detail"] == "No se encontro un equipo con ese id"



def test_get_teams_vacio(session: Session, client: TestClient) -> None:
    respuesta = client.get("/teams/")
    contenido = respuesta.json()
    assert respuesta.status_code == 200
    assert len(contenido) == 0

def test_get_teams(session: Session, client: TestClient)-> None:
    equipo = Equipo(id_equipo = 1, nombre="nombre", pokemons_de_equipo=[])
    session.add(equipo)
    session.commit()
    respuesta = client.get("/teams/")
    contenido = respuesta.json()
    assert respuesta.status_code == 200
    assert len(contenido) == 1


# def test_buscar_team_por_id():
#     teams.append(equipo_con_6_pokemons)
#     response = client.get("/teams/1")
#     assert response.status_code == 200


# def test_buscar_equipo_no_existente():
#     response = client.get("/teams/100")
#     assert response.status_code == 404
#     assert response.json()["detail"] == "No se encontro el equipo"


# def test_actualizar_equipo_existente():
#     teams.append(equipo_con_6_pokemons)
#     response = client.put("/teams", json=equipo_mismo_id)
#     content = response.json()
#     assert response.status_code == 200
#     assert content["id_equipo"] == equipo_mismo_id["id_equipo"]
#     assert content["nombre"] == equipo_mismo_id["nombre"]
#     teams.clear()


# def test_actualizar_equipo_no_existente():
#     response = client.put("/teams", json=equipo)
#     assert response.status_code == 404
#     assert response.json()["detail"] == "No se encontro un equipo con ese id"
