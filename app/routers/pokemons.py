from fastapi import APIRouter, HTTPException
from fastapi import status
from models import Pokemon, Movimiento
from app.routers.moves import buscar_movimiento
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


def cargar_todos_los_pokemon():
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

            cadena_evolutiva_ids = []
            anteriores = []
            id_actual = pokemon_id
            while id_actual in evoluciones and evoluciones[id_actual]["anteriores"]:
                anteriores.extend(evoluciones[id_actual]["anteriores"])
                id_actual = evoluciones[id_actual]["anteriores"][0]
            cadena_evolutiva_ids.extend(reversed(anteriores))
            cadena_evolutiva_ids.append(pokemon_id)
            siguientes = evoluciones.get(pokemon_id, {}).get("siguientes", [])
            cadena_evolutiva_ids.extend(siguientes)

            pokemon = Pokemon(
                pokemon_id=pokemon_id,
                nombre=fila["identifier"],
                imagen=imagen_url,
                tipos=[],
                habilidades=[],
                movimientos_ids=[],
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
                cadena_evolutiva_ids=cadena_evolutiva_ids,
            )
            POKEMON_DATA.append(pokemon)

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
                for pokemon in POKEMON_DATA:
                    if fila["type_id"] in pokemon_tipos_aux.get(pokemon.pokemon_id, []):
                        pokemon.tipos.append(fila["name"])

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
                for pokemon in POKEMON_DATA:
                    if fila["ability_id"] in pokemon_habilidades_aux.get(
                        pokemon.pokemon_id, []
                    ):
                        pokemon.habilidades.append(fila["name"])

    with open(POKEMON_STATS_CSV, newline="", encoding="utf-8") as archivo_csv:
        estadisticas_reader = csv.DictReader(archivo_csv)
        for fila in estadisticas_reader:
            pokemon_id = int(fila["pokemon_id"])
            stat_id = fila["stat_id"]
            base_stat = int(fila["base_stat"])
            pokemon = next(
                (p for p in POKEMON_DATA if p.pokemon_id == pokemon_id), None
            )
            if pokemon:
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

    with open(POKEMON_MOVES_CSV, newline="", encoding="utf-8") as archivo_csv:
        movimientos_reader = csv.DictReader(archivo_csv)

        for fila in movimientos_reader:
            pokemon_id = int(fila["pokemon_id"])
            move_id = int(fila["move_id"])

            for indice_pokemon in range(len(POKEMON_DATA)):
                if POKEMON_DATA[indice_pokemon].pokemon_id == pokemon_id:
                    movimientos_aux = set(POKEMON_DATA[indice_pokemon].movimientos_ids)
                    if move_id not in movimientos_aux:
                        movimientos_aux.add(move_id)
                        POKEMON_DATA[indice_pokemon].movimientos_ids.append(move_id)
                    break
                elif POKEMON_DATA[indice_pokemon].pokemon_id > pokemon_id:
                    break

cargar_todos_los_pokemon()

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
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pokémon no encontrado.")

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
    for a in POKEMON_DATA:
        if a["pokemon_id"] == id:
            POKEMON_DATA.remove(a)
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="No se encontro ese id en nuestros pokemons",
    )
