# incluyan clases de lo que haga falta
from fastapi import APIRouter, HTTPException, status
import csv
from app.routers.pokemons import lista_contenido_limitado
from models import Pokemon, Movimiento, Error

router = APIRouter()

MOVES_CSV = "moves.csv"
MOVES_DAMAGE_CSV = "move_damage_class.csv"
MOVE_EFFECT_CSV = "move_effect.csv"
TYPE_NAMES = "type_names.csv"
ESPANIOL = 7
INGLES = 9


def buscar_movimiento(id):

    with open(MOVES_CSV, "r") as moves:
        datos_csv = csv.DictReader(moves)
        for row in datos_csv:
            if int(row["id"]) == id:
                return Movimiento(
                    id=int(row["id"]),
                    nombre=row["identifier"],
                    tipo=buscar_por_id(row["type_id"], "name", ESPANIOL, TYPE_NAMES),
                    power=(
                        int(row["power"]) if row["power"].strip() else None
                    ),  # comprueba que la casilla no esta vacia
                    accuracy=int(row["accuracy"]) if row["accuracy"].strip() else None,
                    pp=int(row["pp"]),
                    generacion=f"Generation {row['generation_id']}",
                    categoria=buscar_por_id(
                        row["damage_class_id"], "name", ESPANIOL, MOVES_DAMAGE_CSV
                    ),
                    efecto=buscar_por_id(
                        row["effect_id"],
                        "short_effect",
                        INGLES,
                        MOVE_EFFECT_CSV,
                    ),
                    probabilidad_efecto=(
                        row["effect_chance"] if row["effect_chance"].strip() else None
                    ),
                )
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Movement not found"
        )


def buscar_por_id(id, nombre_columna, id_idioma, ruta_archivo):
    with open(ruta_archivo, "r") as entrada:
        datos_csv = csv.DictReader(entrada)
        encabezado = datos_csv.fieldnames  # para ver la primera columna
        for row in datos_csv:
            if row[encabezado[0]] == id and int(row["local_language_id"]) == id_idioma:
                return row[nombre_columna]


# generacion de lista, podria ser movida a otro py
@router.get("/{id}/pokemon")
def getmoves_id_pokemon(id: int) -> list:
    return encontrar_pokemones_por_id_mov(int(id))


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
    with open(
        "pokemon_moves.csv", newline=""
    ) as archivo_movimientos:  # para que se ejecute bien el api,los csv tienen que estar en el mismo directorio que main.py
        lista_movimientos = csv.DictReader(
            archivo_movimientos
        )  # generacion de lista, podria ser movida a otro py, puede no ser llevada ya que pede que exista para el getmoves
        lista_movimientos_filtrada = []
        for elem in lista_movimientos:
            if int(elem["move_id"]) == ID:
                lista_movimientos_filtrada.append(elem)
        for item in lista_contenido_limitado:
            for elem in lista_movimientos_filtrada:
                if item["id"] == int(elem["pokemon_id"]):
                    if int(elem["move_id"]) == ID:
                        if len(lista_final) == 0:
                            lista_final.append(
                                (
                                    {
                                        "id": item["id"],
                                        "nombre": item["nombre"],
                                        "imagen": item["imagen"],
                                        "tipos": item["tipos"],
                                    }
                                )
                            )
                        else:
                            if lista_final[len(lista_final) - 1]["id"] != item["id"]:
                                lista_final.append(
                                    (
                                        {
                                            "id": item["id"],
                                            "nombre": item["nombre"],
                                            "imagen": item["imagen"],
                                            "tipos": item["tipos"],
                                        }
                                    )
                                )
    return lista_final


@router.get("/{id}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def show(id: int) -> Movimiento:
    return buscar_movimiento(id)
