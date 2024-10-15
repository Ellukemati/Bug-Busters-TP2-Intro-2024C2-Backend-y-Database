from fastapi import APIRouter, HTTPException
from fastapi import status
from models import Pokemon
import csv

router = APIRouter()

POKEMON_CSV = "pokemon.csv"
POKEMON_STATS_CSV = "pokemon_stats.csv"
POKEMON_TYPES_CSV = "pokemon_types.csv"
TYPE_NAMES_CSV = "type_names.csv"
POKEMON_ABILITIES_CSV = "pokemon_abilities.csv"
ABILITY_NAMES_CSV = "ability_names.csv"
POKEMON_EVOLUTIONS_CSV = "pokemon_evolutions.csv"

POKEMON_DATA = (
    {}
)  # Diccionario de todos los Pokémon con sus datos cargados, a los que se accede por ID.


def cargar_todos_los_pokemon():
    global POKEMON_DATA

    evoluciones = {}
    with open(POKEMON_EVOLUTIONS_CSV, newline="", encoding="utf-8") as archivo_csv:
        evoluciones_reader = csv.DictReader(archivo_csv)
        for fila in evoluciones_reader:
            pokemon_id = int(fila["id"])
            evolution_id = int(fila["evolution_id"])

            if pokemon_id not in evoluciones:
                evoluciones[pokemon_id] = {"siguientes": [], "anteriores": []}
            evoluciones[pokemon_id]["siguientes"].append(evolution_id)

            if evolution_id not in evoluciones:
                evoluciones[evolution_id] = {"siguientes": [], "anteriores": []}
            evoluciones[evolution_id]["anteriores"].append(pokemon_id)

    with open(POKEMON_CSV, newline="", encoding="utf-8") as archivo_csv:
        pokemon_reader = csv.DictReader(archivo_csv)
        for fila in pokemon_reader:
            pokemon_id = int(fila["id"])
            imagen_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_id}.png"

            cadena_evolutiva = []  # Armado de cadena evolutiva.
            anteriores = []
            id_actual = pokemon_id
            while id_actual in evoluciones and evoluciones[id_actual]["anteriores"]:
                anteriores.extend(evoluciones[id_actual]["anteriores"])
                id_actual = evoluciones[id_actual]["anteriores"][0]
            cadena_evolutiva.extend(reversed(anteriores))
            cadena_evolutiva.append(pokemon_id)
            siguientes = evoluciones.get(pokemon_id, {}).get("siguientes", [])
            cadena_evolutiva.extend(siguientes)

            pokemon = Pokemon(
                pokemon_id=pokemon_id,
                nombre=fila["identifier"],
                imagen=imagen_url,
                tipos=[],
                habilidades=[],
                altura=int(fila["height"]),
                peso=int(fila["weight"]),
                estadisticas={
                    "hp": 0,
                    "attack": 0,
                    "defense": 0,
                    "special-attack": 0,
                    "special-defense": 0,
                    "speed": 0,
                    "accuracy": 0,
                    "evasion": 0,
                },
                cadena_evolutiva=cadena_evolutiva,
            )
            POKEMON_DATA[pokemon_id] = pokemon
    for pokemon in POKEMON_DATA.values():
        print(f"{pokemon.nombre}: {pokemon.cadena_evolutiva}")

    with open(POKEMON_TYPES_CSV, newline="", encoding="utf-8") as archivo_csv:
        tipo_reader = csv.DictReader(archivo_csv)
        pokemon_tipos_aux = {}
        for fila in tipo_reader:
            pokemon_id = int(fila["pokemon_id"])
            tipo_id = fila["type_id"]
            if pokemon_id not in pokemon_tipos_aux:
                pokemon_tipos_aux[pokemon_id] = []
            pokemon_tipos_aux[pokemon_id].append(tipo_id)

    with open(TYPE_NAMES_CSV, newline="", encoding="utf-8") as archivo_csv:
        nombre_tipo_reader = csv.DictReader(archivo_csv)
        for fila in nombre_tipo_reader:
            if fila["local_language_id"] == "7":
                for pokemon_id, tipos_ids in pokemon_tipos_aux.items():
                    if fila["type_id"] in tipos_ids:
                        POKEMON_DATA[pokemon_id].tipos.append(fila["name"])

    with open(POKEMON_ABILITIES_CSV, newline="", encoding="utf-8") as archivo_csv:
        habilidades_reader = csv.DictReader(archivo_csv)
        pokemon_habilidades_aux = {}
        for fila in habilidades_reader:
            pokemon_id = int(fila["pokemon_id"])
            habilidad_id = fila["ability_id"]
            if pokemon_id not in pokemon_habilidades_aux:
                pokemon_habilidades_aux[pokemon_id] = []
            pokemon_habilidades_aux[pokemon_id].append(habilidad_id)

    with open(ABILITY_NAMES_CSV, newline="", encoding="utf-8") as archivo_csv:
        ability_name_reader = csv.DictReader(archivo_csv)
        for fila in ability_name_reader:
            if fila["local_language_id"] == "7":
                for pokemon_id, habilidades_ids in pokemon_habilidades_aux.items():
                    if fila["ability_id"] in habilidades_ids:
                        POKEMON_DATA[pokemon_id].habilidades.append(fila["name"])

    with open(POKEMON_STATS_CSV, newline="", encoding="utf-8") as archivo_csv:
        estadisticas_reader = csv.DictReader(archivo_csv)
        for fila in estadisticas_reader:
            pokemon_id = int(fila["pokemon_id"])
            stat_id = fila["stat_id"]
            base_stat = int(fila["base_stat"])
            pokemon = POKEMON_DATA[pokemon_id]
            if stat_id == "1":
                pokemon.estadisticas["hp"] = base_stat
            elif stat_id == "2":
                pokemon.estadisticas["attack"] = base_stat
            elif stat_id == "3":
                pokemon.estadisticas["defense"] = base_stat
            elif stat_id == "4":
                pokemon.estadisticas["special-attack"] = base_stat
            elif stat_id == "5":
                pokemon.estadisticas["special-defense"] = base_stat
            elif stat_id == "6":
                pokemon.estadisticas["speed"] = base_stat
            elif stat_id == "7":
                pokemon.estadisticas["accuracy"] = base_stat
            elif stat_id == "8":
                pokemon.estadisticas["evasion"] = base_stat


cargar_todos_los_pokemon()


@router.get("/{id}", response_model=Pokemon)
def get_pokemon_by_id(id: int):
    if id in POKEMON_DATA:
        return POKEMON_DATA[id]
    raise HTTPException(status_code=404, detail="Pokémon no encontrado.")
