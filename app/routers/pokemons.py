from fastapi import APIRouter, HTTPException
from app.models import Pokemon
import csv

router = APIRouter()

POKEMON_CSV = "pokemon.csv"
POKEMON_STATS_CSV = "pokemon_stats.csv"
POKEMON_TYPES_CSV = "pokemon_types.csv"
TYPE_NAMES_CSV = "type_names.csv"
POKEMON_ABILITIES_CSV = "pokemon_abilities.csv"
ABILITY_NAMES_CSV = "ability_names.csv"


@router.get("/pokemons/{id}", response_model=Pokemon)
def get_pokemon_by_id(id: int):
    with open(POKEMON_CSV, newline="", encoding="utf-8") as archivo_csv:
        pokemon_reader = csv.DictReader(archivo_csv)
        pokemon_info = None
        for fila in pokemon_reader:
            if int(fila["id"]) == id:
                pokemon_info = fila
                break
        if not pokemon_info:
            raise HTTPException(status_code=404, detail="Pokémon no encontrado.")

    imagen_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png"

    tipos_ids = []
    with open(POKEMON_TYPES_CSV, newline="", encoding="utf-8") as archivo_csv:
        tipo_reader = csv.DictReader(archivo_csv)
        for fila in tipo_reader:
            if int(fila["pokemon_id"]) == id: # Cubre el caso de que el Pokémon tenga más de un tipo.
                tipos_ids.append(fila["type_id"])

    tipos = []
    with open(TYPE_NAMES_CSV, newline="", encoding="utf-8") as archivo_csv:
        nombre_tipo_reader = csv.DictReader(archivo_csv)
        for fila in nombre_tipo_reader:
            if fila["local_language_id"] == "7" and fila["type_id"] in tipos_ids:
                tipos.append(fila["name"])

    habilidades_ids = []
    with open(POKEMON_ABILITIES_CSV, newline="", encoding="utf-8") as archivo_csv:
        habilidades_reader = csv.DictReader(archivo_csv)
        for fila in habilidades_reader:
            if int(fila["pokemon_id"]) == id:
                habilidades_ids.append(fila["ability_id"])

    habilidades = []
    with open(ABILITY_NAMES_CSV, newline="", encoding="utf-8") as archivo_csv:
        ability_name_reader = csv.DictReader(archivo_csv)
        for fila in ability_name_reader:
            if fila["local_language_id"] == "7" and fila["ability_id"] in habilidades_ids:
                habilidades.append(fila["name"])

    estadisticas = {
        "hp": 0,
        "attack": 0,
        "defense": 0,
        "special-attack": 0,
        "special-defense": 0,
        "speed": 0,
        "accuracy": 0,
        "evasion": 0,
    }
    with open(POKEMON_STATS_CSV, newline="", encoding="utf-8") as archivo_csv:
        estadisticas_reader = csv.DictReader(archivo_csv)
        for fila in estadisticas_reader:
            if int(fila["pokemon_id"]) == id:
                stat_id = fila["stat_id"]
                base_stat = int(fila["base_stat"])
                if stat_id == "1":
                    estadisticas["hp"] = base_stat
                elif stat_id == "2":
                    estadisticas["attack"] = base_stat
                elif stat_id == "3":
                    estadisticas["defense"] = base_stat
                elif stat_id == "4":
                    estadisticas["special-attack"] = base_stat
                elif stat_id == "5":
                    estadisticas["special-defense"] = base_stat
                elif stat_id == "6":
                    estadisticas["speed"] = base_stat
                elif stat_id == "7":
                    estadisticas["accuracy"] = base_stat
                elif stat_id == "8":
                    estadisticas["evasion"] = base_stat

    pokemon = Pokemon(
        id=int(pokemon_info["id"]),
        nombre=pokemon_info["identifier"],
        imagen=imagen_url,
        tipos=tipos,
        habilidades=habilidades,
        altura=int(pokemon_info["height"]),
        peso=int(pokemon_info["weight"]),
        estadisticas=estadisticas
    )


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
