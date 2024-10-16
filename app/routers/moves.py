# incluyan clases de lo que haga falta
from fastapi import APIRouter,  HTTPException, status, Request
import csv
from pokemons import pokemons
from pydantic import BaseModel


class Pokemon(BaseModel):
    pokemon_id: int
    nombre: str
    imagen: str
    tipos: list[str]
    habilidades: list[str]
    altura: int
    peso: int
    estadisticas: dict[str, int]
    cadena_evolutiva: list[int]

class Movimiento(BaseModel):
    id: int
    nombre: str
    tipo: str
    power: int
    accuracy: int
    pp: int
    generacion: str
    categoria: str
    efecto: str
    probabilidad_efecto: int | None = None

router = APIRouter()



# generacion de lista, podria ser movida a otro py
@router.get("/{id}/pokemon")
def getmoves_id_pokemon(id: int) -> list[Pokemon]:
    return(encontrar_pokemones_por_id_mov(int(id)))
def encontrar_pokemones_por_id_mov(ID):
    lista_final: list[Pokemon] = []
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