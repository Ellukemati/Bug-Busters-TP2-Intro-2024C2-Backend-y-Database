from fastapi import APIRouter, HTTPException, status
from app.models.pokemon import Pokemon
from app.models.movimiento import Movimiento
from sqlmodel import select
from app.models.error import Error
from app.db.database import SessionDep


router = APIRouter()


@router.get("/{id}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def show(session: SessionDep, id: int) -> Movimiento:
    movimiento = session.exec(select(Movimiento).where(Movimiento.id == id)).first()

    if movimiento:
        return movimiento
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Movimiento not found"
    )


@router.get("/{id}/pokemon", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def getmoves_id_pokemon(session: SessionDep, id: int) -> list[Pokemon]:
    movimiento = session.exec(select(Movimiento).where(Movimiento.id == id)).first()

    if movimiento:
        pokemones = movimiento.pokemon_que_lo_aprenden
        return pokemones
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Movimiento not found"
    )
