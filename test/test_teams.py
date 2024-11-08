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




def test_get_teams(session: Session, client: TestClient) -> None:
    respuesta = client.get("/teams/")
    contenido = respuesta.json()
    assert respuesta.status_code == 200
    assert len(contenido) == 0

