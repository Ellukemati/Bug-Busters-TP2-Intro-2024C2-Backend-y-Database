# incluyan clases de lo que haga falta
from fastapi import APIRouter,  HTTPException, status
import csv
from app.routers.pokemons import lista_contenido_limitado
from models import Pokemon, Movimiento


router = APIRouter()



# generacion de lista, podria ser movida a otro py
@router.get("/{id}/pokemon")
def getmoves_id_pokemon(id: int) -> list:
    return(encontrar_pokemones_por_id_mov(int(id)))

def encontrar_pokemones_por_id_mov(ID):
    lista_final: list[dict] = []
    with open("moves.csv", newline="") as movimientos:
        existe = False
        movs = csv.DictReader(movimientos)
        for elem in movs:
            if int(elem["id"]) == ID:
                existe = True
    if not existe:
        raise HTTPException(status_code=404, detail="Movimiento no encontrado")
    with open("pokemon_moves.csv", newline="") as archivo_movimientos:# para que se ejecute bien el api,los csv tienen que estar en el mismo directorio que main.py
        lista_movimientos = csv.DictReader(archivo_movimientos)# generacion de lista, podria ser movida a otro py, puede no ser llevada ya que pede que exista para el getmoves
        lista_movimientos_filtrada = []
        for elem in lista_movimientos:
            if (int(elem["move_id"]) == ID):
                lista_movimientos_filtrada.append(elem)
        for item in lista_contenido_limitado:
            for elem in lista_movimientos_filtrada:
                if (item["id"] == int(elem["pokemon_id"])):
                    if (int(elem["move_id"]) == ID):
                        if len(lista_final) == 0:
                            lista_final.append(({"id": item["id"], "nombre": item["nombre"], "imagen": item["imagen"], "tipos": item["tipos"]}))
                        else: 
                            if lista_final[len(lista_final) - 1]["id"] != item["id"]:
                                lista_final.append(({"id": item["id"], "nombre": item["nombre"], "imagen": item["imagen"], "tipos": item["tipos"]}))
    return (lista_final)
@router.get("/")
def get_movements():
    return {"Hello": "World"}


@router.get("/{id}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def show(id: int) -> Movimiento:
    return buscar_movimiento(id)


def buscar_movimiento(id):
    movimiento = Movimiento()

    with open("../archivos/moves.csv", "r") as moves:
        datos_csv = csv.reader(moves)
        for row in datos_csv:
            if row["id"] == id:
                movimiento.id = row["id"]
                movimiento.nombre = row["identifier"]
                movimiento.tipo = buscar_por_id(row["type_id"])
                movimiento.power = row["power"]
                movimiento.accuracy = row["accuracy"]
                movimiento.pp = row["pp"]
                movimiento.generacion = f"Generation {row['generation_id']}"
                movimiento.categoria = buscar_por_id(
                    row["damage_class_id"], "name", "archivos/move_damage_prose.csv"
                )
                movimiento.efecto = buscar_por_id(
                    row["effect_id"],
                    "short_effect",
                    "archivos/conquest_move_effect_prose.csv",
                )
            else:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail="Movement not found"
                )
    return movimiento


def buscar_por_id(id, nombre_columna, ruta_archivo):
    with open(ruta_archivo, "r") as entrada:
        datos_csv = csv.reader(entrada)
        for row in datos_csv:
            if row[0] == id and row["local_language_id"] == 9:
                return row[nombre_columna]
