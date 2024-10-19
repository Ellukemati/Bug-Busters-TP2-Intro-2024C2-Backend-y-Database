from models import Pokemon, Naturaleza
from fastapi import APIRouter, HTTPException, status
import csv


router = APIRouter()

pokemons: list[Pokemon] = []


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



Naturalezas: list[Naturaleza] = []
estadisticas = {}


def list_natures():
    with open("stats.csv", mode="r") as estadisticas_file:
        reader = csv.DictReader(estadisticas_file)
        for row in reader:
            estadisticas[row["id"]] = row["identifier"]

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

            Naturalezas.append(naturaleza)


list_natures()


@router.get("/natures")
def show_natures() -> list[Naturaleza]:
    return Naturalezas

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
