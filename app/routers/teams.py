# incluyan clases de lo que haga falta
from fastapi import APIRouter, HTTPException, status
from models import Movimiento, Pokemon, Integrante_pokemon, Equipo, Naturaleza

router = APIRouter()

teams: list[Equipo] = []
movs: list[Movimiento] = []
movs.append(Movimiento(id=1, nombre="nom1", tipo="None", power=2, accuracy=14, pp=3, generacion="None", categoria="None", efecto="None"))
movs.append(Movimiento(id=2, nombre="nom2", tipo="None", power=2, accuracy=14, pp=3, generacion="None", categoria="None", efecto="None"))
movs.append(Movimiento(id=3, nombre="nom3", tipo="None", power=2, accuracy=14, pp=3, generacion="None", categoria="None", efecto="None"))
movs.append(Movimiento(id=4, nombre="nom4", tipo="None", power=2, accuracy=14, pp=3, generacion="None", categoria="None", efecto="None"))
poks: list[Integrante_pokemon] = []
Naturalezas: list[Naturaleza] = []
Naturalezas.append(Naturaleza(id=1, nombre="habi", aumenta_estadistica="puede", reduce_estadistica="puede que no"))
Naturalezas.append(Naturaleza(id=2, nombre="lidad", aumenta_estadistica="si tenes suerte", reduce_estadistica="probablemente"))
Naturalezas.append(Naturaleza(id=3, nombre="sita", aumenta_estadistica="ni lo pienses", reduce_estadistica="no tenes idea"))
poks.append(Integrante_pokemon(id=1, nombre="bulb", naturaleza=Naturalezas[1], movimientos=movs))
teams.append(Equipo(id_equipo=1, nombre="equipo", pokemons_de_equipo=poks))
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
@router.get("/")
def get_teams() -> list[Equipo]:
    return teams
