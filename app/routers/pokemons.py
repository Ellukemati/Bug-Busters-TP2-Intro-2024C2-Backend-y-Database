# incluyan clases de lo que haga falta
from fastapi import APIRouter, HTTPException, status
import csv
from models import Pokemon



router = APIRouter()
# generacion de lista, podria ser movida a otro py
pokemons: list[Pokemon] = []
with open ("pokemon.csv", newline="") as archivo:# para que se ejecute bien el api,los csv tienen que estar en el mismo directorio que main.py
    lista_pokemon = csv.DictReader(archivo)
    imagen = (
        "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/<id>.png"
    )
    for elem in lista_pokemon:
        monstruo = {"tipo": ""}
        with open ("pokemon_types.csv", newline="") as archivos_tipos:
            pokemon_tipo = csv.DictReader(archivos_tipos)
            tps = [-1, -1]
            posicion = 0
            for fila in pokemon_tipo:
                if fila["pokemon_id"] == elem["id"]:
                    tps[posicion] = fila["type_id"]
                    posicion = posicion + 1
            if tps[1] == -1:
                del tps[1]
        with open ("type_names.csv", newline="") as tipos_nombres:
            lista_tipos = csv.DictReader(tipos_nombres)
            for fila in lista_tipos:
                if fila["local_language_id"] == "7":
                    posicion = 0
                    for i in tps:
                        if i == fila["type_id"]:
                            tipo = fila["name"]
                            tipo = tipo.replace("\n", "")
                            tps[posicion] = tipo
                        posicion = posicion + 1
        lista_tps: list[str] = []
        for i in tps:
            lista_tps.append(i)
        if len(tps) == 2:
            monstruo["tipo"] = tps[0] + "," + tps[1]
        else:
            monstruo["tipo"] = tps[0]
        with open ("pokemon_abilities.csv", newline="") as habilidades_pokemon:
            lista_habilidades = csv.DictReader(habilidades_pokemon)
            habilidades = []
            for fila in lista_habilidades:
                if fila["pokemon_id"] == elem["id"]:
                    habilidades.append(fila["ability_id"])
        with open ("ability_names.csv", newline="") as habilidades_nombres:
            lista_habilidades = csv.DictReader(habilidades_nombres)
            lista_filtrada = []
            for fila in lista_habilidades:
                if (fila["local_language_id"] == "7"):
                    lista_filtrada.append(fila)
            habilidades_lista_nombre: list[str] = []
            for pos in habilidades:
                habilidades_lista_nombre.append("a")
            for parte in lista_filtrada:
                posicion = 0
                for fila in habilidades:
                    if (int(fila) == int(parte["ability_id"])):
                        habilidades_lista_nombre[posicion] = parte["name"]
                    posicion = posicion + 1
            i=0
            while (i < len(habilidades)):
                habilidades[i] = habilidades_lista_nombre[i]
                i = i + 1
        dicc_stats = {"hp": 0,
                      "attack": 0,
                      "defense": 0,
                      "special-attack": 0,
                      "special-defense": 0,
                      "speed": 0,
                      "accuracy": 0,
                      "evasion": 0,}  
        id_evolutivo=elem["id"]
        orden_evolutivo=[]
        orden_evolutivo.append(int(elem["order"]))
        temp_id=int(elem["id"])
        temp_orden=int(elem["order"])
        with open ("pokemon.csv", newline="") as archivo2:
            segunda_lista_pokemones = csv.DictReader(archivo2)
            finalizo = False
            fin_preevo = False
            fin_evo = False
            while not finalizo:
                for linea in segunda_lista_pokemones:
                    if (int(linea["id"]) == (int(elem["id"]) - 1) and not fin_preevo):
                        if int(linea["order"]) == (int(elem["order"]) - 1):
                            orden_evolutivo.append(int(linea["order"]))
                            temp_id=int(linea["id"])
                            temp_orden=int(linea["order"])
                        else:
                            fin_preevo = True
                            temp_id=int(elem["id"])
                            temp_orden=int(elem["order"])
                    elif (int(linea["id"]) == (int(elem["id"]) + 1) and not fin_evo):
                        if int(linea["order"]) == (int(elem["order"]) + 1):
                            orden_evolutivo.append(int(linea["order"]))
                            temp_id=int(linea["id"])
                            temp_orden=int(linea["order"])
                        else:
                            fin_evo = True
                            temp_id=int(elem["id"])
                            temp_orden=int(elem["order"])
                if (fin_preevo and fin_evo):
                    finalizo = True
        orden_evolutivo.sort()
        with open("stats.csv", newline="") as estadisticas:
            lista_estadisticas = csv.DictReader(estadisticas)
            for fila in lista_estadisticas:
                with open ("pokemon_stats.csv", newline="") as stats:
                    lista_stats = csv.DictReader(stats)
                    for linea in lista_stats:
                        if (linea["pokemon_id"] == elem["id"] and linea["stat_id"] == fila["id"]):
                            if int(fila["id"]) == 1:
                                dicc_stats["hp"] = int(linea["base_stat"])
                            elif int(fila["id"]) == 2:
                                dicc_stats["attack"] = int(linea["base_stat"])
                            elif int(fila["id"]) == 3:
                                dicc_stats["defense"] = int(linea["base_stat"])
                            elif int(fila["id"]) == 4:
                                dicc_stats["special-attack"] = int(linea["base_stat"])
                            elif int(fila["id"]) == 5:
                                dicc_stats["special-defense"] = int(linea["base_stat"])
                            elif int(fila["id"]) == 6:
                                dicc_stats["speed"] = int(linea["base_stat"])
                            elif int(fila["id"]) == 7:
                                dicc_stats["accuracy"] = int(linea["base_stat"])
                            elif int(fila["id"]) == 8:
                                dicc_stats["evasion"] = int(linea["base_stat"])
        
        pokemons.append(
            Pokemon(
                pokemon_id=int(elem["id"]),
                nombre=elem["identifier"],
                imagen=imagen.replace("<id>", elem["id"]),
                tipos=lista_tps,
                habilidades=habilidades_lista_nombre,
                altura=int(elem["height"]),
                peso=int(elem["weight"]),
                estadisticas=dicc_stats,
                cadena_evolutiva=orden_evolutivo
            )
        )

 
def generar_lista(lista):
    lista_contenido_limitado = []
    for elem in lista:
        lista_contenido_limitado.append({"id": elem.pokemon_id, "nombre": elem.nombre, "imagen": elem.imagen, "tipos": elem.tipos})
    return lista_contenido_limitado




# apartir de este punto implementar los endpoints
@router.get("/")
def get_pokemon() -> list:
    return generar_lista(pokemons)
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

