# incluyan clases de lo que haga falta
from fastapi import APIRouter#,  HTTPException, status
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