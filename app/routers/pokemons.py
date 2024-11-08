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


