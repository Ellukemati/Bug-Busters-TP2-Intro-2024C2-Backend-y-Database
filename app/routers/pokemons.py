# incluyan clases de lo que haga falta
from models import Pokemon
from fastapi import APIRouter, HTTPException, status
import csv


router = APIRouter()
# generacion de lista, podria ser movida a otro py
pokemons: list[Pokemon] = []
with open ("pokemon.csv", newline="") as archivo:# para que se ejecute bien el api,los csv tienen que estar en el mismo directorio que main.py
    lista_pokemon = csv.DictReader(archivo)
    imagen = (
        "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/<id>.png"
    )
    for elem in lista_pokemon:
        monstruo = {"tipo": ""}
        with open ("pokemon_types.csv", newline="") as archivos_tipos:
            pokemon_tipo = csv.DictReader(archivos_tipos)
            tps = [-1, -1]
            posicion = 0
            for fila in pokemon_tipo:
                if fila["pokemon_id"] == elem["id"]:
                    tps[posicion] = fila["type_id"]
                    posicion = posicion + 1
            if tps[1] == -1:
                del tps[1]
        with open ("type_names.csv", newline="") as tipos_nombres:
            lista_tipos = csv.DictReader(tipos_nombres)
            for fila in lista_tipos:
                if fila["local_language_id"] == "7":
                    posicion = 0
                    for i in tps:
                        if i == fila["type_id"]:
                            tipo = fila["name"]
                            tipo = tipo.replace("\n", "")
                            tps[posicion] = tipo
                        posicion = posicion + 1
        if len(tps) == 2:
            monstruo["tipo"] = tps[0] + "," + tps[1]
        else:
            monstruo["tipo"] = tps[0]
        pokemons.append(
            Pokemon(
                id=elem["id"],
                nombre=elem["identifier"],
                imagen=imagen.replace("<id>", elem["id"]),
                tipo=monstruo["tipo"],
            )
        )

 





# apartir de este punto implementar los endpoints
@router.get("/getpokemon/")
def get_pokemon() -> list[Pokemon]:
    return pokemons
@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_pokemon(pokemon: Pokemon) -> Pokemon:
    for a in pokemons:
        if a.id == pokemon.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe un pokemon con ese id",
            )
    pokemons.append(pokemon)
    return pokemon

