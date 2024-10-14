# incluyan clases de lo que haga falta
from models import Pokemon
from fastapi import APIRouter, HTTPException, status


router = APIRouter()


pokemons: list[Pokemon] = []


@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_pokemon(pokemon: Pokemon) -> Pokemon:
    for a in pokemons:
        if a.pokemon_id == pokemon.pokemon_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe un pokemon con ese id",
            )
    pokemons.append(pokemon)
    return pokemon
