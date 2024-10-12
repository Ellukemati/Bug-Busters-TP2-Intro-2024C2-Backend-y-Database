# incluyan clases de lo que haga falta
from models import Pokemon
from fastapi import APIRouter, HTTPException, status


router = APIRouter()

# es necesaria la que este la lista de pokemons inicializada
pokemons: list[Pokemon] = (
    []
)  # <--- borrar cuando se implemente la lista de pokemons con su correspondiente procesamiento


# apartir de este punto implementar los endpoints
@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_pokemon(pokemon: Pokemon) -> Pokemon:
    for a in pokemons:
        if a.id == pokemon.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe un pokemon con ese id",
            )
    pokemons.append(pokemon)
    return pokemon
