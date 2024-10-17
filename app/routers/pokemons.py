
from fastapi import APIRouter, HTTPException, status
import csv
from models import Pokemon



router = APIRouter()

pokemons: list[Pokemon] = []
POKEMON_DATA = (
    {}
)  # Diccionario de todos los Pokémon con sus datos cargados, a los que se accede por ID.


def cargar_todos_los_pokemon():

    evoluciones = {}
    with open("pokemon_evolutions.csv", newline="", encoding="utf-8") as archivo_csv:
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

    with open("pokemon.csv", newline="", encoding="utf-8") as archivo_csv:
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
            pokemons.append(pokemon)

    with open("pokemon_types.csv", newline="", encoding="utf-8") as archivo_csv:
        tipo_reader = csv.DictReader(archivo_csv)
        pokemon_tipos_aux = {}
        for fila in tipo_reader:
            pokemon_id = int(fila["pokemon_id"])
            tipo_id = fila["type_id"]
            if pokemon_id not in pokemon_tipos_aux:
                pokemon_tipos_aux[pokemon_id] = []
            pokemon_tipos_aux[pokemon_id].append(tipo_id)

    with open("type_names.csv", newline="", encoding="utf-8") as archivo_csv:
        nombre_tipo_reader = csv.DictReader(archivo_csv)
        for fila in nombre_tipo_reader:
            if fila["local_language_id"] == "7":
                for pokemon_id, tipos_ids in pokemon_tipos_aux.items():
                    if fila["type_id"] in tipos_ids:
                        for elem in pokemons:
                            if elem.pokemon_id == pokemon_id:
                                elem.tipos.append(fila["name"])

    with open("pokemon_abilities.csv", newline="", encoding="utf-8") as archivo_csv:
        habilidades_reader = csv.DictReader(archivo_csv)
        pokemon_habilidades_aux = {}
        for fila in habilidades_reader:
            pokemon_id = int(fila["pokemon_id"])
            habilidad_id = fila["ability_id"]
            if pokemon_id not in pokemon_habilidades_aux:
                pokemon_habilidades_aux[pokemon_id] = []
            pokemon_habilidades_aux[pokemon_id].append(habilidad_id)

    with open("ability_names.csv", newline="", encoding="utf-8") as archivo_csv:
        ability_name_reader = csv.DictReader(archivo_csv)
        for fila in ability_name_reader:
            if fila["local_language_id"] == "7":
                for pokemon_id, habilidades_ids in pokemon_habilidades_aux.items():
                    if fila["ability_id"] in habilidades_ids:
                        for elem in pokemons:
                            if elem.pokemon_id == pokemon_id:
                                elem.habilidades.append(fila["name"])

    with open("pokemon_stats.csv", newline="", encoding="utf-8") as archivo_csv:
        estadisticas_reader = csv.DictReader(archivo_csv)
        for fila in estadisticas_reader:
            pokemon_id = int(fila["pokemon_id"])
            stat_id = fila["stat_id"]
            base_stat = int(fila["base_stat"])
            for elem in pokemons:
                if elem.pokemon_id == pokemon_id:
                    if stat_id == "1":
                        elem.estadisticas["hp"] = base_stat
                    elif stat_id == "2":
                        elem.estadisticas["attack"] = base_stat
                    elif stat_id == "3":
                        elem.estadisticas["defense"] = base_stat
                    elif stat_id == "4":
                        elem.estadisticas["special-attack"] = base_stat
                    elif stat_id == "5":
                        elem.estadisticas["special-defense"] = base_stat
                    elif stat_id == "6":
                        elem.estadisticas["speed"] = base_stat
                    elif stat_id == "7":
                        elem.estadisticas["accuracy"] = base_stat
                    elif stat_id == "8":
                        elem.estadisticas["evasion"] = base_stat

lista_contenido_limitado = []
cargar_todos_los_pokemon()
def generar_lista(lista):
    lista_contenido_limitado = []
    for elem in lista:
        lista_contenido_limitado.append({"id": elem.pokemon_id, "nombre": elem.nombre, "imagen": elem.imagen, "tipos": elem.tipos})
    return lista_contenido_limitado
@router.get("/")
def get_pokemon() -> list:
    return generar_lista(pokemons)
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


@router.delete("/{id}")
def borrar_pokemon(id: int):
    for a in pokemons:
        if a["pokemon_id"] == id:
            pokemons.remove(a)
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="No se encontro ese id en nuestros pokemons",
    )
