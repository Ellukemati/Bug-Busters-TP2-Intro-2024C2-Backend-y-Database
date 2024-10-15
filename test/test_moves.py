from fastapi.testclient import TestClient
from models import Movimiento
from main import app

client = TestClient(app)


def test_obtener_movimiento_existente():
    movimiento_existente: Movimiento = {
        "id": 190,
        "nombre": "octazooka",
        "tipo": "Water",
        "power": 65,
        "accuracy": 85,
        "pp": 10,
        "generacion": "Generation 2",
        "categoria": "special",
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
        "categoria": "status",
        "efecto": "Immediately ends wild battles.  Forces trainers to switch Pokémon.",
        "probabilidad_efecto": None,
    }
    response = client.get("moves/46")
    content = response.json()
    assert response.status_code == 200
    assert content == movimiento_existente
