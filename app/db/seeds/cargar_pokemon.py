import csv
from sqlmodel import Session, create_engine

from app.models.pokemon import Pokemon
from app.models.pokemonMovimiento import PokemonMovimiento

POKEMON_CSV = "pokemon.csv"
POKEMON_STATS_CSV = "pokemon_stats.csv"
STATS_CSV = "stats.csv"
POKEMON_TYPES_CSV = "pokemon_types.csv"
TYPE_NAMES_CSV = "type_names.csv"
POKEMON_ABILITIES_CSV = "pokemon_abilities.csv"
ABILITY_NAMES_CSV = "ability_names.csv"
POKEMON_EVOLUTIONS_CSV = "pokemon_evolutions.csv"
POKEMON_MOVES_CSV = "pokemon_moves.csv"
MOVES_CSV = "moves.csv"
MOVE_EFFECT_CSV = "move_effect_prose.csv"

DATABASE_URL = "sqlite:///app/db/database.py"
engine = create_engine(DATABASE_URL)

def cargar_pokemon(session: Session):
    pokemons = {}
    ids_movimientos_por_pokemon = {}
    with open(POKEMON_CSV, mode="r", encoding="utf-8") as archivo_csv:
        pokemon_reader = csv.DictReader(archivo_csv)
        for fila in pokemon_reader:
            pokemon_id = int(fila["id"])
            pokemon = Pokemon(
                id=pokemon_id,
                nombre=fila["identifier"],
                url_imagen=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{fila["id"]}.png",
                altura=int(fila["height"]),
                peso=int(fila["weight"]),
                tipo_1="",
                tipo_2=None,
                habilidad_1="",
                habilidad_2=None,
                habilidad_3=None,
                estadistica_hp=0,
                estadistica_attack=0,
                estadistica_defense=0,
                estadistica_special_attack=0,
                estadistica_special_defense=0,
                estadistica_speed=0,
                posibles_movimientos=[]
            )
            pokemons[pokemon_id] = pokemon
            ids_movimientos_por_pokemon[pokemon_id] = set()

    # Carga de estadísticas
    estadisticas_nombres = {}
    with open(STATS_CSV, mode="r", encoding="utf-8") as archivo_csv:
        stats_reader = csv.DictReader(archivo_csv)
        for fila in stats_reader:
            stat_id = int(fila["id"])
            estadisticas_nombres[stat_id] = fila["identifier"]

    with open(POKEMON_STATS_CSV, mode="r", encoding="utf-8") as archivo_csv:
        estadisticas_reader = csv.DictReader(archivo_csv)
        for fila in estadisticas_reader:
            pokemon_id = int(fila["pokemon_id"])
            stat_id = int(fila["stat_id"])
            base_stat = int(fila["base_stat"])
            nombre_estadistica = estadisticas_nombres[stat_id]
            pokemon = pokemons[pokemon_id]

            if nombre_estadistica == "hp":
                pokemon.estadistica_hp = base_stat
            elif nombre_estadistica == "attack":
                pokemon.estadistica_attack = base_stat
            elif nombre_estadistica == "defense":
                pokemon.estadistica_defense = base_stat
            elif nombre_estadistica == "special-attack":
                pokemon.estadistica_special_attack = base_stat
            elif nombre_estadistica == "special-defense":
                pokemon.estadistica_special_defense = base_stat
            elif nombre_estadistica == "speed":
                pokemon.estadistica_speed = base_stat

    # Carga de tipos
    tipos_nombres = {}
    with open(TYPE_NAMES_CSV, mode="r", encoding="utf-8") as archivo_csv:
        type_names_reader = csv.DictReader(archivo_csv)
        for fila in type_names_reader:
            if fila["local_language_id"] == "7":
                type_id = int(fila["type_id"])
                tipos_nombres[type_id] = fila["name"]
            elif fila["type_id"] == "10002":
                tipos_nombres[10002] = "Oscuro"

    with open(POKEMON_TYPES_CSV, mode="r", encoding="utf-8") as archivo_csv:
        pokemon_types_reader = csv.DictReader(archivo_csv)
        for fila in pokemon_types_reader:
            pokemon_id = int(fila["pokemon_id"])
            type_id = int(fila["type_id"])
            nombre_tipo = tipos_nombres[type_id]
            pokemon = pokemons[pokemon_id]

            if not pokemon.tipo_1:
                pokemon.tipo_1 = nombre_tipo
            elif not pokemon.tipo_2:
                pokemon.tipo_2 = nombre_tipo

    # Carga de habilidades
    habilidades_nombres = {}
    with open(ABILITY_NAMES_CSV, mode="r", encoding="utf-8") as archivo_csv:
        ability_names_reader = csv.DictReader(archivo_csv)
        for fila in ability_names_reader:
            if fila["local_language_id"] == "7":
                ability_id = int(fila["ability_id"])
                habilidades_nombres[ability_id] = fila["name"]

    with open(POKEMON_ABILITIES_CSV, mode="r", encoding="utf-8") as archivo_csv:
        pokemon_abilities_reader = csv.DictReader(archivo_csv)
        for fila in pokemon_abilities_reader:
            pokemon_id = int(fila["pokemon_id"])
            ability_id = int(fila["ability_id"])
            habilidad_nombre = habilidades_nombres[ability_id]
            pokemon = pokemons[pokemon_id]

            if not pokemon.habilidad_1:
                pokemon.habilidad_1 = habilidad_nombre
            elif not pokemon.habilidad_2:
                pokemon.habilidad_2 = habilidad_nombre
            elif not pokemon.habilidad_3:
                pokemon.habilidad_3 = habilidad_nombre

    session.add_all(pokemons.values())
    session.commit()

    # Carga de las relaciones Pokémon-Movimientos
    with open(POKEMON_MOVES_CSV, mode="r", encoding="utf-8") as archivo_csv:
        pokemon_moves_reader = csv.DictReader(archivo_csv)
        for fila in pokemon_moves_reader:
            pokemon_id = int(fila["pokemon_id"])
            move_id = int(fila["move_id"])

            if move_id in ids_movimientos_por_pokemon[pokemon_id]:
                continue

            pokemon_movimiento = PokemonMovimiento(
                pokemon_id=pokemon_id,
                movimiento_id=move_id
            )
            ids_movimientos_por_pokemon[pokemon_id].add(move_id)
            session.add(pokemon_movimiento)

        session.commit()
