# incluyan clases de lo que haga falta
from fastapi import APIRouter, HTTPException, status
from models import Movimiento
from main import app
from app.routers.pokemons import lista_contenido_limitado
from fastapi.testclient import TestClient
client = TestClient(app)



def test_get_moves_id_pokemon_3():
    respuesta = client.get("/moves/3/pokemon")
    contenido = respuesta.json()
    assert respuesta.status_code == 200
    assert contenido[0]["id"] == 35
    assert contenido[1]["nombre"] == "clefable"
    assert contenido[0]["imagen"] == "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/35.png"
    assert contenido[0]["tipos"][0] == "Hada"
def test_get_moves_id_pokemon_176():
    respuesta = client.get("/moves/176/pokemon")
    contenido = respuesta.json()
    assert respuesta.status_code == 200
    assert len(contenido) == 3
    assert contenido[0]["id"] == 137
    assert contenido[1]["id"] == 233
    assert contenido[2]["id"] == 474
def test_get_moves_id_pokemon_10001():
    respuesta = client.get("/moves/10001/pokemon")
    contenido = respuesta.json()
    assert respuesta.status_code == 200
    assert len(contenido) == 0
def test_get_moves_id_pokemon_vacio():
    respuesta = client.get("/moves/80000/pokemon")
    assert respuesta.status_code == 404
def test_get_moves_id_pokemon_vacio_2():
    respuesta = client.get("/moves/900/pokemon")
    assert respuesta.status_code == 404
def test_get_moves_id_pokemon_176():
    respuesta = client.get("/moves/25/pokemon")
    contenido = respuesta.json()
    assert respuesta.status_code == 200
    assert len(contenido) == 233
def test_obtener_movimiento_existente():
    movimiento_existente: Movimiento = {
        "id": 190,
        "nombre": "octazooka",
        "power": 65,
        "accuracy": 85,
        "pp": 10,
        "generacion": "Generation 2",
        "categoria": "especial",
        "efecto": "Has a $effect_chance% chance to lower the target's accuracy by one stage.",
        "probabilidad_efecto": 50,
    }

    response = client.get("moves/190")
    content = response.json()
    assert response.status_code == 200
    assert content == movimiento_existente


def test_obtener_movimento_no_existente():
    response = client.get("moves/850")
    assert response.status_code == 404


def test_obtener_movimiento_existente_con_casillas_vacias():
    movimiento_existente: Movimiento = {
        "id": 46,
        "nombre": "roar",
        "tipo": "Normal",
        "power": None,
        "accuracy": None,
        "pp": 20,
        "generacion": "Generation 1",
        "categoria": "estado",
        "efecto": "Immediately ends wild battles.  Forces trainers to switch Pokémon.",
        "probabilidad_efecto": None,
    }
    response = client.get("moves/46")
    content = response.json()
    assert response.status_code == 200
    assert content == movimiento_existente
