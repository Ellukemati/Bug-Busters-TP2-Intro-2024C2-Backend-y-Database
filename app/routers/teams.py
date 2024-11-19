# incluyan clases de lo que haga falta
from fastapi import APIRouter, HTTPException, status
from app.models.error import Error
from app.models.equipos import EquipoPublic, Equipo, Integrante_pokemon, EquipoCreate, Integrante_pokemonCreate
from app.models.movimiento import Movimiento
from app.models.pokemon import Pokemon
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
def post_team(session: SessionDep, team: EquipoCreate) -> EquipoPublic:
    teams = session.exec(select(Equipo).where(Equipo.id_equipo == team.id_equipo)).first()
    if not teams:
        equipo = Equipo(nombre = team.nombre, id_equipo = team.id_equipo)
        for integrante in team.pokemons_de_equipo:
            if(integrante.equipo_id != equipo.id_equipo):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="un integrante no comparte id con el equipo")
            pokemon = session.exec(select(Pokemon).where(Pokemon.id == integrante.pokemon_id)).first()
            if not pokemon:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El pokemon no existe")
            naturaleza = session.exec(select(Naturaleza).where(Naturaleza.id == integrante.naturaleza_id)).first()
            if not naturaleza:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La naturaleza no existe")
            miembro = Integrante_pokemon(id=integrante.id, equipo_id = integrante.equipo_id, naturaleza_id = integrante.naturaleza_id, pokemon_id = integrante.pokemon_id, naturaleza = naturaleza.nombre)
            for movimiento in integrante.movimientos_ids:
                moves = session.exec(select(Movimiento).where(Movimiento.id == movimiento)).first()
                if not moves:
                    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El movimiento no existe")
                aprende = False
                for mov in pokemon.posibles_movimientos:
                    if mov.id == movimiento:
                        aprende = True
                if not aprende:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El pokemon no aprende el movimiento")
                miembro.movimientos.append(moves)
            equipo.pokemons_de_equipo.append(miembro)
        if(len(equipo.pokemons_de_equipo) > 6):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Tiene demasiados integrantes")
        session.add(equipo)
        session.commit()
        session.refresh(equipo)
        return equipo
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="ID de equipo ya ocupado"
        )


@router.get("/")
def get_teams(session: SessionDep) -> list[EquipoPublic]:
    query = select(Equipo)
    equipos = session.exec(query)
    return equipos


@router.get("/{id}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def show_id_team(session: SessionDep, id: int) -> EquipoPublic:
    equipo = session.exec(select(Equipo).where(Equipo.id_equipo == id)). first()
    if equipo:
        return equipo
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Equipo no encontrado")


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

@router.put("/{id}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def update(session: SessionDep, id: int, equipo_actualizado: EquipoCreate) -> EquipoPublic:
    equipo = session.exec(select(Equipo).where(Equipo.id_equipo == id)).first()
    if equipo is not None:
        equipo_final = Equipo(nombre = equipo_actualizado.nombre, id_equipo = equipo_actualizado.id_equipo)
        for integrante in equipo_actualizado.pokemons_de_equipo:
            if(integrante.equipo_id != equipo_actualizado.id_equipo):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="un integrante no comparte id con el equipo")
            pokemon = session.exec(select(Pokemon).where(Pokemon.id == integrante.pokemon_id)).first()
            if not pokemon:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El pokemon no existe")
            naturaleza = session.exec(select(Naturaleza).where(Naturaleza.id == integrante.naturaleza_id)).first()
            if not naturaleza:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La naturaleza no existe")
            miembro = Integrante_pokemon(id=integrante.id, equipo_id = integrante.equipo_id, naturaleza_id = integrante.naturaleza_id, pokemon_id = integrante.pokemon_id, naturaleza = naturaleza.nombre)
            for movimiento in integrante.movimientos_ids:
                moves = session.exec(select(Movimiento).where(Movimiento.id == movimiento)).first()
                if not moves:
                    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El movimiento no existe")
                aprende = False
                for mov in pokemon.posibles_movimientos:
                    if mov.id == movimiento:
                        aprende = True
                if not aprende:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El pokemon no aprende el movimiento")
                miembro.movimientos.append(moves)
            equipo_final.pokemons_de_equipo.append(miembro)
        if(len(equipo_final.pokemons_de_equipo) > 6):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Tiene demasiados integrantes")
        equipo.id_equipo = equipo_final.id_equipo
        equipo.nombre = equipo_final.nombre
        equipo.pokemons_de_equipo = equipo_final.pokemons_de_equipo
        session.add(equipo)
        session.commit()
        session.refresh(equipo)
        return equipo
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Equipo no encontrado")
