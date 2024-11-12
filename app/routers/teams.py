# incluyan clases de lo que haga falta
from fastapi import APIRouter, HTTPException, status, Depends
from models import Error
from app.models.movimiento import Movimiento
from app.models.equipos import Equipo, Integrante_pokemon, EquipoPublic, EquipoBase
from app.models.naturaleza import Naturaleza
from sqlmodel import select, Session, insert
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
def post_team(session: SessionDep, team: Equipo) -> EquipoPublic:
    equipo = session.exec(select(Equipo).where(Equipo.id_equipo == team.id_equipo)).first()
    if equipo is None:
        session.add(team)
        session.commit()
        session.refresh(team)
        return team
    raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe un equipo con ese id",
            )



@router.get("/")
def get_teams() -> list[Equipo]:
    return teams


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

