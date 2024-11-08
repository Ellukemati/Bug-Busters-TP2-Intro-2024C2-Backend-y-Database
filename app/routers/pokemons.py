from fastapi import APIRouter, HTTPException, status
from app.models.error import Error
from app.models.pokemon import Pokemon, PokemonBase
from app.models.movimiento import Movimiento
from sqlmodel import select
from app.db.database import SessionDep



router = APIRouter()


POKEMON_DATA: list[Pokemon] = []  # Lista "Base de datos", con todos los Pokémon.


lista_contenido_limitado = []


def generar_lista(lista):
    lista_contenido_limitado.clear()
    for elem in lista:
        lista_contenido_limitado.append(
            {
                "id": elem.pokemon_id,
                "nombre": elem.nombre,
                "imagen": elem.imagen,
                "tipos": elem.tipos,
            }
        )
    return lista_contenido_limitado


@router.get("/")
def get_pokemon() -> list:
    return generar_lista(POKEMON_DATA)

@router.get("/{id}")
def get_pokemon_by_id(session: SessionDep, id: int) -> Pokemon:
    pokemon = session.exec(select(Pokemon).where(Pokemon.id == id)).first()
    if pokemon:
        return pokemon
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Pokémon no encontrado"
        )


@router.get("/{id}/moves", response_model=list[Movimiento])
def obtener_movimientos_pokemon(session: SessionDep,id: int) -> list[Movimiento]:
    pokemon = session.exec(select(Pokemon).where(Pokemon.id == id)).first()
        
    if pokemon:
        movimientos = pokemon.posibles_movimientos
        return movimientos
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Pokémon no encontrado."
    )


@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_pokemon(session: SessionDep, pokemon_nuevo: PokemonBase) -> PokemonBase:
    pokemon = Pokemon(
        nombre=pokemon_nuevo.nombre,
        url_imagen=pokemon_nuevo.url_imagen,
        altura=pokemon_nuevo.altura,
        peso=pokemon_nuevo.peso,
        tipo_1=pokemon_nuevo.tipo_1,
        tipo_2=pokemon_nuevo.tipo_2,
        habilidad_1=pokemon_nuevo.habilidad_1,
        habilidad_2=pokemon_nuevo.habilidad_2,
        habilidad_3=pokemon_nuevo.habilidad_3,
        estadistica_hp=pokemon_nuevo.estadistica_hp,
        estadistica_attack=pokemon_nuevo.estadistica_attack,
        estadistica_defense=pokemon_nuevo.estadistica_defense,
        estadistica_special_attack=pokemon_nuevo.estadistica_special_attack,
        estadistica_special_defense=pokemon_nuevo.estadistica_special_defense,
        estadistica_speed=pokemon_nuevo.estadistica_speed,
        id_evolucion_anterior=pokemon_nuevo.id_evolucion_anterior,
        id_evolucion_siguiente=pokemon_nuevo.id_evolucion_siguiente,
    )
    session.add(pokemon)
    session.commit()
    session.refresh(pokemon)
    return pokemon


@router.delete("/{id}")
def borrar_pokemon(session: SessionDep, id: int) -> Pokemon:
    pokemon_eliminar = session.exec(select(Pokemon).where(Pokemon.id == id)).first()
    if pokemon_eliminar:
        session.delete(pokemon_eliminar)
        session.commit()
        return pokemon_eliminar

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="No se encontro ese id en nuestros pokemons",
    )
