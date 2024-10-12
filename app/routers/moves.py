# incluyan clases de lo que haga falta
from fastapi import APIRouter#,  HTTPException, status
from models import Movimiento, Pokemon

router = APIRouter()

# generacion de lista, podria ser movida a otro py, puede no ser llevada ya que existe para 
poke_mov: list[Movimiento] = []
archivo = open(
    "pokemon_moves.csv", "r"
)  # para que se ejecute bien el api,los csv tienen que estar en el mismo directorio que main.py
lista_movimientos = archivo.readlines()
archivo.close()
lista_movimientos.pop(0)




pokemones: list[Pokemon] = []
archivo = open(
    "pokemon.csv", "r"
)  # para que se ejecute bien el api,los csv tienen que estar en el mismo directorio que main.py
lista_pokemon = archivo.readlines()
archivo.close()

lista_pokemon.pop(0)
imagen = (
    "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/<id>.png"
)
for elem in lista_pokemon:
    individuo = elem.split(",")
    tipos_nombres = open("type_names.csv", "r")
    lista_tipos = tipos_nombres.readlines()
    tipos_nombres.close()
    monstruo = {"indice": 1, "nombre": "B", "link_img": "C", "tipo": ""}
    archivos_tipos = open("pokemon_types.csv", "r")
    pokemon_tipo = archivos_tipos.readlines()
    archivos_tipos.close()
    tps = [-1, -1]
    posicion = 0
    for i in pokemon_tipo:
        tipos = i.split(",")
        if tipos[0] == individuo[0]:
            tps[posicion] = tipos[1]
            posicion = posicion + 1
    if tps[1] == -1:
        del tps[1]
    tipos_nombres = open("type_names.csv", "r")
    lista_tipos = tipos_nombres.readlines()
    tipos_nombres.close()
    for i in lista_tipos:
        lista_elem_tipos = i.split(",")
        if lista_elem_tipos[1] == "7":
            posicion = 0
            for i in tps:
                if i == lista_elem_tipos[0]:
                    tipo = lista_elem_tipos[2]
                    tipo = tipo.replace("\n", "")
                    tps[posicion] = tipo
                posicion = posicion + 1
    try:
        monstruo["tipo"] = tps[0] + "," + tps[1]
    except:
        monstruo["tipo"] = tps[0]
    pokemones.append(
        Pokemon(
            num_indice=individuo[0],
            nombre=individuo[1],
            link_imagen=imagen.replace("<id>", individuo[0]),
            tipo=monstruo["tipo"],
        )
    )
# apartir de este punto implementar los endpoints
@router.get("/{id}")
def getmoves_id_pokemon(id: int) -> Movimiento:
    return encontrar_pokemones_por_id_mov(int(id))

def encontrar_pokemones_por_id_mov(ID):
    lista_final: list[Pokemon] = []
    i = 0
    while i < len(lista_movimientos):
        borro = False
        if lista_movimientos[i][2] != ID:
            lista_movimientos.pop(i)
            borro = True
        if not borro:
            i = i + 1 
    for item in pokemones:
        aprende_el_mov = False
        for elem in lista_movimientos:
            if item[num_indice] == elem[2]:
                if lista_final[-1][num_indice] != item[num_indice]:
                    aprende_el_mov = True
        if aprende_el_mov:
            lista_final.append(item)
    return lista_final