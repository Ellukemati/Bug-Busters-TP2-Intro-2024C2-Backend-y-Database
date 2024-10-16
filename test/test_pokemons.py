from fastapi.testclient import TestClient

from main import app

client = TestClient(app)
def test_get_pokemons():
    respuesta = client.get("/pokemon/")
    contenido = respuesta.json()
    assert respuesta.status_code == 200
    assert contenido[0].id_pokemon == 1
    assert contenido[0].nombre == "bulbasaur"
    assert contenido[0].imagen == "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png"
    assert contenido[0].id_pokemon == "veneno,planta"