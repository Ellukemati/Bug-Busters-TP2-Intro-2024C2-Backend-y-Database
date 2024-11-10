from fastapi import APIRouter, HTTPException, status
from app.models.pokemon import Pokemon
from app.models.movimiento import Movimiento
from sqlmodel import select
from app.models.error import Error
from app.db.database import SessionDep


router = APIRouter()


@router.get("/{id}", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def show(session: SessionDep, id: int) -> Movimiento:
    movimiento = session.exec(select(Movimiento).where(Movimiento.id == id)).first()

    if movimiento:
        return movimiento
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Movimiento not found"
    )


@router.get("/{id}/pokemon", responses={status.HTTP_404_NOT_FOUND: {"model": Error}})
def getmoves_id_pokemon(session: SessionDep, id: int) -> list[Pokemon]:
    movimiento = session.exec(select(Movimiento).where(Movimiento.id == id)).first()

    if movimiento:
        pokemones = movimiento.pokemon_que_lo_aprenden
        return pokemones
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Movimiento not found"
    )


# def encontrar_pokemones_por_id_mov(ID):
#     lista_final: list[dict] = []
#     with open("moves.csv", newline="") as movimientos:
#         existe = False
#         movs = csv.DictReader(movimientos)
#         for elem in movs:
#             if int(elem["id"]) == ID:
#                 existe = True
#     if not existe:
#         raise HTTPException(status_code=404, detail="Movimiento no encontrado")
#     with open(
#         "pokemon_moves.csv", newline=""
#     ) as archivo_movimientos:  # para que se ejecute bien el api,los csv tienen que estar en el mismo directorio que main.py
#         lista_movimientos = csv.DictReader(
#             archivo_movimientos
#         )  # generacion de lista, podria ser movida a otro py, puede no ser llevada ya que pede que exista para el getmoves
#         lista_movimientos_filtrada = []
#         for elem in lista_movimientos:
#             if int(elem["move_id"]) == ID:
#                 lista_movimientos_filtrada.append(elem)
#         for item in lista_contenido_limitado:
#             for elem in lista_movimientos_filtrada:
#                 if item["id"] == int(elem["pokemon_id"]):
#                     if int(elem["move_id"]) == ID:
#                         if len(lista_final) == 0:
#                             lista_final.append(
#                                 (
#                                     {
#                                         "id": item["id"],
#                                         "nombre": item["nombre"],
#                                         "imagen": item["imagen"],
#                                         "tipos": item["tipos"],
#                                     }
#                                 )
#                             )
#                         else:
#                             if lista_final[len(lista_final) - 1]["id"] != item["id"]:
#                                 lista_final.append(
#                                     (
#                                         {
#                                             "id": item["id"],
#                                             "nombre": item["nombre"],
#                                             "imagen": item["imagen"],
#                                             "tipos": item["tipos"],
#                                         }
#                                     )
#                                 )
#     return lista_final
