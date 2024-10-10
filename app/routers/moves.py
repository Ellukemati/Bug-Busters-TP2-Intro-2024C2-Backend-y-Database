from models import Movimiento, Error
from fastapi import APIRouter, HTTPException, status
import csv

router = APIRouter()


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
