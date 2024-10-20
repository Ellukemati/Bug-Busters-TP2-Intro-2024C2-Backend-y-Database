from models import Movimiento, Error
from fastapi import APIRouter, HTTPException, status
import csv

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


@router.get("/{id}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def show(id: int) -> Movimiento:
    return buscar_movimiento(id)
