from main import app
from fastapi.testclient import TestClient
from app.models.movimiento import Movimiento
from app.models.pokemon import Pokemon
from app.models.pokemonMovimiento import PokemonMovimiento
from sqlmodel import Session
from test.jsons import movimiento_id_176,pokemons_que_aprenden_176,relaciones, movimiento_sin_pokemones_que_lo_aprendan

client = TestClient(app)


def test_get_moves_id_pokemon_176(session: Session, client: TestClient):
    movimiento = Movimiento(**movimiento_id_176)
    pokemones = [Pokemon(**data) for data in pokemons_que_aprenden_176]
    pokemon_movimientos = [PokemonMovimiento(**data) for data in relaciones]

    session.add(movimiento)
    session.add_all(pokemones)
    session.add_all(pokemon_movimientos)
    session.commit()
    respuesta = client.get("/moves/176/pokemon")
    contenido = respuesta.json()
    assert respuesta.status_code == 200
    assert len(contenido) == 3
    assert contenido[0] == pokemons_que_aprenden_176[2]
    assert contenido[1] == pokemons_que_aprenden_176[1]
    assert contenido[2] == pokemons_que_aprenden_176[0]


def test_get_moves_id_pokemon_10001(session: Session, client: TestClient):
    movimiento = Movimiento(**movimiento_sin_pokemones_que_lo_aprendan)
    session.add(movimiento)
    session.commit()
    respuesta = client.get("/moves/10001/pokemon")
    contenido = respuesta.json()
    assert respuesta.status_code == 200
    assert len(contenido) == 0


def test_get_moves_id_pokemon_inexistente():
    respuesta = client.get("/moves/80000/pokemon")
    assert respuesta.status_code == 404


def test_obtener_movimiento_existente(session: Session, client: TestClient):
    movimiento_existente = Movimiento(
        id=190,
        nombre="Pulpocañón",
        tipo="Agua",
        power=65,
        accuracy=85,
        pp=10,
        generacion="Generation 2",
        categoria="especial",
        efecto="Has a $effect_chance% chance to lower the target's accuracy by one stage.",
        probabilidad_efecto=50,
    )
    session.add(movimiento_existente)
    session.commit()
    response = client.get("moves/190")
    content = response.json()
    assert response.status_code == 200
    assert content["id"] == movimiento_existente.id
    assert content["nombre"] == movimiento_existente.nombre
    assert content["tipo"] == movimiento_existente.tipo
    assert content["power"] == movimiento_existente.power
    assert content["accuracy"] == movimiento_existente.accuracy
    assert content["pp"] == movimiento_existente.pp
    assert content["generacion"] == movimiento_existente.generacion
    assert content["categoria"] == movimiento_existente.categoria
    assert content["efecto"] == movimiento_existente.efecto
    assert content["probabilidad_efecto"] == movimiento_existente.probabilidad_efecto


def test_obtener_movimento_no_existente(session: Session, client: TestClient):
    response = client.get("moves/850")
    assert response.status_code == 404


def test_obtener_movimiento_existente_con_casillas_vacias(
    session: Session, client: TestClient
):
    movimiento_existente = Movimiento(
        id=46,
        nombre="Rugido",
        tipo="Normal",
        power=None,
        accuracy=None,
        pp=20,
        generacion="Generation 1",
        categoria="estado",
        efecto="Immediately ends wild battles.  Forces trainers to switch Pokémon.",
        probabilidad_efecto=None,
    )
    session.add(movimiento_existente)
    session.commit()

    response = client.get("moves/46")
    content = response.json()
    assert response.status_code == 200
    assert content["id"] == movimiento_existente.id
    assert content["nombre"] == movimiento_existente.nombre
    assert content["tipo"] == movimiento_existente.tipo
    assert content["power"] == movimiento_existente.power
    assert content["accuracy"] == movimiento_existente.accuracy
    assert content["pp"] == movimiento_existente.pp
    assert content["generacion"] == movimiento_existente.generacion
    assert content["categoria"] == movimiento_existente.categoria
    assert content["efecto"] == movimiento_existente.efecto
    assert content["probabilidad_efecto"] == movimiento_existente.probabilidad_efecto
