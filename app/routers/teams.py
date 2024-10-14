# incluyan clases de lo que haga falta
from fastapi import APIRouter, HTTPException, status
from models import Pokemon, Equipo


router = APIRouter()

teams: list[Equipo] = []
# apartir de este punto implementar los endpoints


@router.post("/", status_code=status.HTTP_201_CREATED)
def post_team(team: Equipo) -> list[Equipo]:
    for equipo_existente in teams:
        if equipo_existente.id_equipo == team.id_equipo:
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
