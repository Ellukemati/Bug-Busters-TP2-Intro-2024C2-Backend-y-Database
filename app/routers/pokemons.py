from fastapi import APIRouter, HTTPException, status
from app.models.pokemon import Pokemon
from app.models.movimiento import Movimiento
from app.models.naturaleza import Naturaleza
from app.routers.funciones import buscar_movimiento
import csv

router = APIRouter()

POKEMON_CSV = "pokemon.csv"
POKEMON_STATS_CSV = "pokemon_stats.csv"
POKEMON_TYPES_CSV = "pokemon_types.csv"
TYPE_NAMES_CSV = "type_names.csv"
POKEMON_ABILITIES_CSV = "pokemon_abilities.csv"
ABILITY_NAMES_CSV = "ability_names.csv"
POKEMON_EVOLUTIONS_CSV = "pokemon_evolutions.csv"
POKEMON_MOVES_CSV = "pokemon_moves.csv"

POKEMON_DATA: list[Pokemon] = []  # Lista "Base de datos", con todos los Pokémon.




lista_contenido_limitado = []


def generar_lista(lista):
    lista_contenido_limitado.clear()
    for elem in lista:
        lista_contenido_limitado.append(
            {
                "id": elem.pokemon_id,
                "nombre": elem.nombre,
                "imagen": elem.imagen,
                "tipos": elem.tipos,
            }
        )
    return lista_contenido_limitado


def get_pokemon_para_test() -> list:  # {
    return generar_lista(
        POKEMON_DATA
    )  # para asegurar funcionalidad del test get moves/id/pokemon


get_pokemon_para_test()  # }


@router.get("/{id}", response_model=Pokemon)
def get_pokemon_by_id(id: int):
    for pokemon in POKEMON_DATA:
        if pokemon.pokemon_id == id:
            return pokemon
    raise HTTPException(status_code=404, detail="Pokémon no encontrado.")


@router.get("/")
def get_pokemon() -> list:
    return generar_lista(POKEMON_DATA)


@router.get("/{id}", response_model=Pokemon)
def obtener_pokemon_por_id(id: int):
    for pokemon in POKEMON_DATA:
        if pokemon.pokemon_id == id:
            return pokemon
    raise HTTPException(status_code=404, detail="Pokémon no encontrado.")


@router.get("/{id}/moves", response_model=list[Movimiento])
def obtener_movimientos_pokemon(id: int) -> list[Movimiento]:
    movimientos = []
    pokemon = None
    for poke in POKEMON_DATA:
        if poke.pokemon_id == id:
            pokemon = poke
            break
    if not pokemon:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Pokémon no encontrado."
        )
    for movimiento_id in pokemon.movimientos_ids:
        movimiento = buscar_movimiento(movimiento_id)
        movimientos.append(movimiento)
    return movimientos


@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_pokemon(pokemon: Pokemon) -> Pokemon:
    for a in POKEMON_DATA:
        pokemon_id = a.get("pokemon_id") if isinstance(a, dict) else a.pokemon_id
        if pokemon_id == pokemon.pokemon_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe un pokemon con ese id",
            )
    POKEMON_DATA.append(pokemon)
    return pokemon


@router.delete("/{id}")
def borrar_pokemon(id: int):
    for indice, pokemon_existente in enumerate(POKEMON_DATA):
        id_pokemon_existente = (
            pokemon_existente.get("pokemon_id")
            if isinstance(pokemon_existente, dict)
            else pokemon_existente.pokemon_id
        )
        if id_pokemon_existente == id:
            POKEMON_DATA.remove(pokemon_existente)
            return pokemon_existente
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="No se encontro ese id en nuestros pokemons",
    )
