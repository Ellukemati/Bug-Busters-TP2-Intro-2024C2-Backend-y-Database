# incluyan clases de lo que haga falta
from fastapi import APIRouter, HTTPException, status
from app.models.pokemon import Pokemon
from app.models.movimiento import Movimiento
from app.models.naturaleza import Naturaleza
from app.models.equipos import EquipoPublic, Integrante_pokemon, Equipo
from sqlmodel import Session, select
from app.db.database import SessionDep
import csv


router = APIRouter()


@router.get("/")
def get_teams(session: SessionDep) -> list[EquipoPublic]:
    query = select(Equipo)
    equipos = session.exec(query)
    return equipos
