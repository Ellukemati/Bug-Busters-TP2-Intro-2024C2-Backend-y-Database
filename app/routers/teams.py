# incluyan clases de lo que haga falta
from fastapi import APIRouter, HTTPException, status
from app.models.movimiento import Movimiento
from app.models.pokemon import Pokemon
from app.models.naturaleza import Naturaleza
from app.models.equipos import EquipoPublic, Equipo, Integrante_pokemon
from sqlmodel import Session, select
from app.db.database import SessionDep
import csv


router = APIRouter()

teams: list[Equipo] = []
# apartir de este punto implementar los endpoints
estadisticas = {}



@router.get("/natures")
def show_natures(Session: SessionDep) -> list[Naturaleza]:
    query = select(Naturaleza)
    naturalezas = Session.exec(query)
    return naturalezas


@router.post("/", status_code=status.HTTP_201_CREATED)
def post_team(team: Equipo) -> list[Equipo]:
    for equipo_existente in teams:
        id_equipo_existente = (
            equipo_existente.get("id_equipo")
            if isinstance(equipo_existente, dict)
            else equipo_existente.id_equipo
        )
        if id_equipo_existente == team.id_equipo:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe un equipo con ese id",
            )
    if len(team.pokemons_de_equipo) > 6:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Puedes tener un maximo de seis pokemons",
        )

    teams.append(team)
    return teams


@router.get("/")
def get_teams(session: SessionDep) -> list[EquipoPublic]:
    query = select(Equipo)
    equipos = session.exec(query)
    return equipos


@router.get("/{id}")
def show_id_team(id: int) -> Equipo:
    for indice, equipo_existente in enumerate(teams):
        id_equipo_existente = (
            equipo_existente.get("id_equipo")
            if isinstance(equipo_existente, dict)
            else equipo_existente.id_equipo
        )
        if id_equipo_existente == id:
            return teams[indice]
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro el equipo"
    )


@router.delete("/{id}")
def borrar_equipo(id: int) -> Equipo:
    for indice, equipo_existente in enumerate(teams):
        id_equipo_existente = (
            equipo_existente.get("id_equipo")
            if isinstance(equipo_existente, dict)
            else equipo_existente.id_equipo
        )
        if id_equipo_existente == id:
            teams.pop(indice)
            return equipo_existente
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="No se encontro un equipo con ese id",
    )

@router.put("/")
def update(equipo_actualizado: Equipo) -> Equipo:
    for indice, equipo_existente in enumerate(teams):
        id_equipo_existente = (
            equipo_existente.get("id_equipo")
            if isinstance(equipo_existente, dict)
            else equipo_existente.id_equipo
        )
        if id_equipo_existente == equipo_actualizado.id_equipo:
            teams[indice] = equipo_actualizado
            return equipo_actualizado
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="No se encontro un equipo con ese id",
    )

