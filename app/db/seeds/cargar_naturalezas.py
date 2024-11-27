import csv
from app.db.database import Session
from app.models.naturaleza import Naturaleza



estadisticas = {}

with open("stats.csv", mode="r") as estadisticas_file:
    reader = csv.DictReader(estadisticas_file)
    for row in reader:
        estadisticas[row["id"]] = row["identifier"]

def cargar_naturalezas(session: Session):
    with open("natures.csv", mode="r") as naturalezas_file:
        reader = csv.DictReader(naturalezas_file)
        for row in reader:
            id_aumenta = row["increased_stat_id"]
            id_disminuye = row["decreased_stat_id"]
            nombre_aumenta = estadisticas.get(id_aumenta)
            nombre_disminuye = estadisticas.get(id_disminuye)
            naturaleza = Naturaleza(
                id=int(row["id"]),
                nombre=row["identifier"],
                aumenta_estadistica=nombre_aumenta,
                reduce_estadistica=nombre_disminuye,
            )
            session.add(naturaleza)
        session.commit()