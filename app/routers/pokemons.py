# incluyan clases de lo que haga falta
from fastapi import APIRouter  # , HTTPException, status
from models import Pokemon

router = APIRouter()
# generacion de lista, podria ser movida a otro py
pokemones: list[Pokemon] = []
archivo = open('pokemon.csv', 'r')
lista_pokemon = archivo.readlines()
archivo.close()
lista_pokemon.pop(0)
imagen = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/<id>.png"
for elem in lista_pokemon:
    individuo = elem.split(",")
    tipos_nombres = open("type_names.csv", 'r')
    lista_tipos = tipos_nombres.readlines()
    tipos_nombres.close()
    monstruo = {'indice': 1, 'nombre': 'B', 'link_img': 'C', 'tipo': ""}
    archivos_tipos = open("pokemon_types.csv", 'r')
    pokemon_tipo = archivos_tipos.readlines()
    archivos_tipos.close()
    tps=[-1,-1]
    posicion = 0
    for i in pokemon_tipo:
        tipos = i.split(",")
        if (tipos[0] == individuo[0]):
            tps[posicion] = tipos[1]
            posicion = (posicion + 1)
    if (tps[1] == -1):
        del(tps[1])
    tipos_nombres = open("type_names.csv", 'r')
    lista_tipos = tipos_nombres.readlines()
    tipos_nombres.close()
    for i in lista_tipos:
        lista_elem_tipos = i.split(",")
        if (lista_elem_tipos[1] == "7"):
            posicion = 0
            for i in tps:
                if (i == lista_elem_tipos[0]):
                    tipo = lista_elem_tipos[2]
                    tipo = tipo.replace('\n', '')
                    tps[posicion] = tipo
                posicion = (posicion + 1)
    try:
        monstruo['tipo']= tps[0] + ',' + tps[1]
    except:
        monstruo['tipo']= tps[0]
    pokemones.append(Pokemon(num_indice=individuo[0], nombre=individuo[1], link_imagen=imagen.replace("<id>", individuo[0]), tipo=monstruo['tipo']))

# apartir de este punto implementar los endpoints
@router.get("/getpokemon/")
def get_pokemon() -> list[Pokemon]:
    return pokemones