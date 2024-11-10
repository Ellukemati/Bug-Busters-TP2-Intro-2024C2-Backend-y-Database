import csv
from app.db.database import Session
from app.models.movimiento import Movimiento

MOVES_CSV = "moves.csv"
MOVE_NAMES = "move_names.csv"
MOVES_DAMAGE_CSV = "move_damage_class.csv"
MOVE_EFFECT_CSV = "move_effect_prose.csv"
TYPE_NAMES = "type_names.csv"
ESPANIOL = 7
INGLES = 9


def buscar_por_id(id, nombre_columna, id_idioma, ruta_archivo):
    if ruta_archivo == TYPE_NAMES and int(id) == 10002:
        return "Oscuro"
    with open(ruta_archivo, "r") as entrada:
        datos_csv = csv.DictReader(entrada)
        encabezado = datos_csv.fieldnames  # para ver la primera columna
        for row in datos_csv:
            if row[encabezado[0]] == id and int(row["local_language_id"]) == id_idioma:
                return row[nombre_columna]
    return None


def cargar_movimientos(session: Session):
    with open(MOVES_CSV, "r") as moves:
        datos_csv = csv.DictReader(moves)
        for row in datos_csv:
            movimiento = Movimiento(
                id=int(row["id"]),
                nombre=buscar_por_id(row["id"], "name", ESPANIOL, MOVE_NAMES),
                tipo=buscar_por_id(row["type_id"], "name", ESPANIOL, TYPE_NAMES),
                power=(
                    int(row["power"]) if row["power"].strip() else None
                ),  # comprueba que la casilla no esta vacia
                accuracy=int(row["accuracy"]) if row["accuracy"].strip() else None,
                pp=int(row["pp"]) if row["pp"].strip() else None,
                generacion=f"Generación {row['generation_id']}",
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
            session.add(movimiento)
        session.commit()
