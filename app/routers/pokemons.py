# incluyan clases de lo que haga falta
from models import Pokemon
from fastapi import APIRouter, HTTPException, status


router = APIRouter()

# es necesaria la que este la lista de pokemons inicializada
pokemons: list[Pokemon] = (
    []
)  # <--- borrar cuando se implemente la lista de pokemons con su correspondiente procesamiento


# apartir de este punto implementar los endpoints
@router.post("/")
def crear_pokemon(pokemon: Pokemon) -> Pokemon:
    pokemons.append(pokemon)
    return pokemon
