# incluyan clases de lo que haga falta
from fastapi import APIRouter#,  HTTPException, status
from models import Movimiento, Pokemon
import csv

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
        if len(tps) == 2:
            monstruo["tipo"] = tps[0] + "," + tps[1]
        else:
            monstruo["tipo"] = tps[0]
        pokemons.append(
            Pokemon(
                id=elem["id"],
                nombre=elem["identifier"],
                imagen=imagen.replace("<id>", elem["id"]),
                tipo=monstruo["tipo"],
            )
        )
@router.get("/{id}/pokemon")
def getmoves_id_pokemon(id: int) -> list[Pokemon]:
    return(encontrar_pokemones_por_id_mov(int(id)))
def encontrar_pokemones_por_id_mov(ID):
    lista_final: list[Pokemon] = []
    with open("pokemon_moves.csv", newline="") as archivo_movimientos:# para que se ejecute bien el api,los csv tienen que estar en el mismo directorio que main.py
        lista_movimientos = csv.DictReader(archivo_movimientos)# generacion de lista, podria ser movida a otro py, puede no ser llevada ya que pede que exista para el getmoves
        lista_movimientos_filtrada = []
        for elem in lista_movimientos:
            if (int(elem["move_id"]) == ID):
                lista_movimientos_filtrada.append(elem)
        for item in pokemons:
            for elem in lista_movimientos_filtrada:
                if (item.id == int(elem["pokemon_id"])):
                    if (int(elem["move_id"]) == ID):
                        if len(lista_final) == 0:
                            lista_final.append(
                                Pokemon(
                                    id=item.id,
                                    nombre=item.nombre,
                                    imagen=item.imagen,
                                    tipo=item.tipo,
                                )
                            )
                        else: 
                            if lista_final[len(lista_final) - 1].id != item.id:
                                lista_final.append(
                                    Pokemon(
                                        id=item.id,
                                        nombre=item.nombre,
                                        imagen=item.imagen,
                                        tipo=item.tipo,
                                    )
                                )
    return (lista_final)