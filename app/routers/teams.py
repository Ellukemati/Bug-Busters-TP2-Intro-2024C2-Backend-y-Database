# incluyan clases de lo que haga falta
from fastapi import APIRouter, HTTPException, status
from models import Movimiento, Pokemon, Integrante_pokemon, Equipo, Naturaleza, Error
from app.models.equipos import EquipoPublic
from sqlmodel import select, Session
from app.db.database import SessionDep
import csv


router = APIRouter()

teams: list[Equipo] = []
# apartir de este punto implementar los endpoints
Naturalezas: list[Naturaleza] = []
estadisticas = {}

with open("stats.csv", mode="r") as estadisticas_file:
    reader = csv.DictReader(estadisticas_file)
    for row in reader:
        estadisticas[row["id"]] = row["identifier"]
with open("natures.csv", mode="r") as naturalezas_file:
    reader = csv.DictReader(naturalezas_file)
    for row in reader:
        id_aumenta = row["increased_stat_id"]
        id_disminuye = row["decreased_stat_id"]
        nombre_aumenta = estadisticas.get(id_aumenta)
        nombre_disminuye = estadisticas.get(id_disminuye)
        naturaleza = Naturaleza(
            id=int(row["id"]),
            nombre=row["identifier"],
            aumenta_estadistica=nombre_aumenta,
            reduce_estadistica=nombre_disminuye,
        )
        Naturalezas.append(naturaleza)


@router.get("/natures")
def show_natures() -> list[Naturaleza]:
    return Naturalezas


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
def get_teams() -> list[Equipo]:
    return teams


@router.get("/{id}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def show_id_team(session: SessionDep, id: int) -> EquipoPublic:
    equipo = session.exec(select(EquipoPublic).where(EquipoPublic.id_equipo == id)). first()
    if equipo:
        return equipo
    raise HTTPException(status_code=status.HTTP_NOT_FOUND, detail="Equipo no encontrado")


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

