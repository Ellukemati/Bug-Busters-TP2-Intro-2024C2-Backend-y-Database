# incluyan clases de lo que haga falta
from fastapi import APIRouter, HTTPException, status
from models import Movimiento, Pokemon, Integrante_pokemon, Equipo, Naturaleza


router = APIRouter()

teams: list[Equipo] = []
# apartir de este punto implementar los endpoints


@router.post("/", status_code=status.HTTP_201_CREATED)
def post_team(team: Equipo) -> list[Equipo]:
    for equipo_existente in teams:
        if equipo_existente["id_equipo"] == team.id_equipo:
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


@router.get("/{id}")
def show_id_team(id: int) -> Equipo:
    for equipo in teams:
        if equipo["id_equipo"] == id:
            return equipo
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="No se encontro el equipo"
    )


@router.delete("/{id}")
def borrar_equipo(id: int) -> Equipo:
    for equipo in teams:
        if equipo["id_equipo"] == id:
            teams.remove(equipo)
            return equipo
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="No se encontro un equipo con ese id",
    )


@router.put("/")
def update(equipo_actualizado: Equipo) -> Equipo:
    for indice, equipo_existente in enumerate(teams):
        if equipo_existente["id_equipo"] == equipo_actualizado.id_equipo:
            teams[indice] = equipo_actualizado
            return equipo_actualizado
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="No se encontro un equipo con ese id",
    )
