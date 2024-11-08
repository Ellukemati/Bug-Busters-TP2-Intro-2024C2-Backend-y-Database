from fastapi import APIRouter, HTTPException, status
import csv
from app.routers.pokemons import lista_contenido_limitado
from models import Error
from app.models.pokemon import Pokemon
from app.models.movimiento import Movimiento
from app.routers.funciones import buscar_movimiento

router = APIRouter()

MOVES_CSV = "moves.csv"
MOVES_DAMAGE_CSV = "move_damage_class.csv"
MOVE_EFFECT_CSV = "move_effect.csv"
TYPE_NAMES = "type_names.csv"
ESPANIOL = 7
INGLES = 9


@router.get("/{id}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def show(id: int) -> Movimiento:
    return buscar_movimiento(id)


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
