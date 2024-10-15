from fastapi.testclient import TestClient
from models import Pokemon, Equipo, Naturaleza, Movimiento, Integrante_pokemon
from main import app
from app.routers.teams import teams

client = TestClient(app)


def test_crear_teams_seis_pokemons():
    equipo_con_6_pokemons = {
        "id_equipo": 1,
        "nombre": "Equipo Elite",
        "pokemons_de_equipo": [
            {
                "id": 25,
                "nombre": "Pikachu",
                "naturaleza": {
                    "id": 1,
                    "nombre": "Activa",
                    "aumenta_estadistica": "Velocidad",
                    "reduce_estadistica": "Defensa",
                },
                "movimientos": [
                    {
                        "id": 1,
                        "nombre": "Impactrueno",
                        "tipo": "Eléctrico",
                        "power": 40,
                        "accuracy": 100,
                        "pp": 30,
                        "generacion": "I",
                        "categoria": "Especial",
                        "efecto": "Parálisis",
                        "probabilidad_efecto": 10,
                    },
                    {
                        "id": 2,
                        "nombre": "Rayo",
                        "tipo": "Eléctrico",
                        "power": 90,
                        "accuracy": 100,
                        "pp": 15,
                        "generacion": "I",
                        "categoria": "Especial",
                        "efecto": "Parálisis",
                        "probabilidad_efecto": 10,
                    },
                ],
            },
            {
                "id": 6,
                "nombre": "Charizard",
                "naturaleza": {
                    "id": 2,
                    "nombre": "Audaz",
                    "aumenta_estadistica": "Ataque",
                    "reduce_estadistica": "Defensa",
                },
                "movimientos": [
                    {
                        "id": 3,
                        "nombre": "Llamarada",
                        "tipo": "Fuego",
                        "power": 110,
                        "accuracy": 85,
                        "pp": 5,
                        "generacion": "I",
                        "categoria": "Especial",
                        "efecto": "Quemadura",
                        "probabilidad_efecto": 30,
                    }
                ],
            },
            {
                "id": 9,
                "nombre": "Blastoise",
                "naturaleza": {
                    "id": 3,
                    "nombre": "Modesta",
                    "aumenta_estadistica": "Ataque Especial",
                    "reduce_estadistica": "Ataque",
                },
                "movimientos": [
                    {
                        "id": 4,
                        "nombre": "Hidrobomba",
                        "tipo": "Agua",
                        "power": 110,
                        "accuracy": 80,
                        "pp": 5,
                        "generacion": "I",
                        "categoria": "Especial",
                        "efecto": "Ninguno",
                        "probabilidad_efecto": None,
                    }
                ],
            },
            {
                "id": 3,
                "nombre": "Venusaur",
                "naturaleza": {
                    "id": 4,
                    "nombre": "Serena",
                    "aumenta_estadistica": "Defensa Especial",
                    "reduce_estadistica": "Ataque",
                },
                "movimientos": [
                    {
                        "id": 5,
                        "nombre": "Solar Rayo",
                        "tipo": "Planta",
                        "power": 120,
                        "accuracy": 100,
                        "pp": 10,
                        "generacion": "I",
                        "categoria": "Especial",
                        "efecto": "Ninguno",
                        "probabilidad_efecto": None,
                    }
                ],
            },
            {
                "id": 94,
                "nombre": "Gengar",
                "naturaleza": {
                    "id": 5,
                    "nombre": "Miedosa",
                    "aumenta_estadistica": "Velocidad",
                    "reduce_estadistica": "Defensa",
                },
                "movimientos": [
                    {
                        "id": 6,
                        "nombre": "Bola Sombra",
                        "tipo": "Fantasma",
                        "power": 80,
                        "accuracy": 100,
                        "pp": 15,
                        "generacion": "II",
                        "categoria": "Especial",
                        "efecto": "Ninguno",
                        "probabilidad_efecto": None,
                    }
                ],
            },
            {
                "id": 149,
                "nombre": "Dragonite",
                "naturaleza": {
                    "id": 6,
                    "nombre": "Firme",
                    "aumenta_estadistica": "Ataque",
                    "reduce_estadistica": "Defensa Especial",
                },
                "movimientos": [
                    {
                        "id": 7,
                        "nombre": "Puño Fuego",
                        "tipo": "Fuego",
                        "power": 100,
                        "accuracy": 100,
                        "pp": 15,
                        "generacion": "II",
                        "categoria": "Físico",
                        "efecto": "Ninguno",
                        "probabilidad_efecto": None,
                    }
                ],
            },
        ],
    }

    response = client.post("/teams", json=equipo_con_6_pokemons)
    assert response.status_code == 201
    data = response.json()

    equipo_creado = data[0]
    assert equipo_creado["id_equipo"] == equipo_con_6_pokemons["id_equipo"]
    assert equipo_creado["nombre"] == equipo_con_6_pokemons["nombre"]


def test_crear_team_con_siete_pokemons():
    equipo_siete_pokemons = {
        "id_equipo": 2,
        "nombre": "Equipo Sobrecargado",
        "pokemons_de_equipo": [
            {
                "id": 25,
                "nombre": "Pikachu",
                "naturaleza": {
                    "id": 1,
                    "nombre": "Activa",
                    "aumenta_estadistica": "Velocidad",
                    "reduce_estadistica": "Defensa",
                },
                "movimientos": [
                    {
                        "id": 1,
                        "nombre": "Impactrueno",
                        "tipo": "Eléctrico",
                        "power": 40,
                        "accuracy": 100,
                        "pp": 30,
                        "generacion": "I",
                        "categoria": "Especial",
                        "efecto": "Parálisis",
                        "probabilidad_efecto": 10,
                    }
                ],
            },
            {
                "id": 6,
                "nombre": "Charizard",
                "naturaleza": {
                    "id": 2,
                    "nombre": "Audaz",
                    "aumenta_estadistica": "Ataque",
                    "reduce_estadistica": "Defensa",
                },
                "movimientos": [
                    {
                        "id": 3,
                        "nombre": "Llamarada",
                        "tipo": "Fuego",
                        "power": 110,
                        "accuracy": 85,
                        "pp": 5,
                        "generacion": "I",
                        "categoria": "Especial",
                        "efecto": "Quemadura",
                        "probabilidad_efecto": 30,
                    }
                ],
            },
            {
                "id": 9,
                "nombre": "Blastoise",
                "naturaleza": {
                    "id": 3,
                    "nombre": "Modesta",
                    "aumenta_estadistica": "Ataque Especial",
                    "reduce_estadistica": "Ataque",
                },
                "movimientos": [
                    {
                        "id": 4,
                        "nombre": "Hidrobomba",
                        "tipo": "Agua",
                        "power": 110,
                        "accuracy": 80,
                        "pp": 5,
                        "generacion": "I",
                        "categoria": "Especial",
                        "efecto": "Ninguno",
                        "probabilidad_efecto": None,
                    }
                ],
            },
            {
                "id": 3,
                "nombre": "Venusaur",
                "naturaleza": {
                    "id": 4,
                    "nombre": "Serena",
                    "aumenta_estadistica": "Defensa Especial",
                    "reduce_estadistica": "Ataque",
                },
                "movimientos": [
                    {
                        "id": 5,
                        "nombre": "Solar Rayo",
                        "tipo": "Planta",
                        "power": 120,
                        "accuracy": 100,
                        "pp": 10,
                        "generacion": "I",
                        "categoria": "Especial",
                        "efecto": "Ninguno",
                        "probabilidad_efecto": None,
                    }
                ],
            },
            {
                "id": 94,
                "nombre": "Gengar",
                "naturaleza": {
                    "id": 5,
                    "nombre": "Miedosa",
                    "aumenta_estadistica": "Velocidad",
                    "reduce_estadistica": "Defensa",
                },
                "movimientos": [
                    {
                        "id": 6,
                        "nombre": "Bola Sombra",
                        "tipo": "Fantasma",
                        "power": 80,
                        "accuracy": 100,
                        "pp": 15,
                        "generacion": "II",
                        "categoria": "Especial",
                        "efecto": "Ninguno",
                        "probabilidad_efecto": None,
                    }
                ],
            },
            {
                "id": 149,
                "nombre": "Dragonite",
                "naturaleza": {
                    "id": 6,
                    "nombre": "Firme",
                    "aumenta_estadistica": "Ataque",
                    "reduce_estadistica": "Defensa Especial",
                },
                "movimientos": [
                    {
                        "id": 7,
                        "nombre": "Puño Fuego",
                        "tipo": "Fuego",
                        "power": 100,
                        "accuracy": 100,
                        "pp": 15,
                        "generacion": "II",
                        "categoria": "Físico",
                        "efecto": "Ninguno",
                        "probabilidad_efecto": None,
                    }
                ],
            },
            {
                "id": 4,
                "nombre": "Gyarados",
                "naturaleza": {
                    "id": 7,
                    "nombre": "Bashful",
                    "aumenta_estadistica": "Defensa",
                    "reduce_estadistica": "Ataque",
                },
                "movimientos": [
                    {
                        "id": 8,
                        "nombre": "Tierra",
                        "tipo": "Tierra",
                        "power": 80,
                        "accuracy": 100,
                        "pp": 15,
                        "generacion": "IV",
                        "categoria": "Físico",
                        "efecto": "Ninguno",
                        "probabilidad_efecto": None,
                    }
                ],
            },
        ],
    }

    response = client.post("/teams", json=equipo_siete_pokemons)

    assert response.status_code == 400
    assert response.json()["detail"] == "Puedes tener un maximo de seis pokemons"


def test_crear_equipo_mismo_id():
    equipo_mismo_id = {
        "id_equipo": 1,
        "nombre": "Equipo Filete",
        "pokemons_de_equipo": [
            {
                "id": 25,
                "nombre": "Pikachu",
                "naturaleza": {
                    "id": 1,
                    "nombre": "Activa",
                    "aumenta_estadistica": "Velocidad",
                    "reduce_estadistica": "Defensa",
                },
                "movimientos": [
                    {
                        "id": 1,
                        "nombre": "Impactrueno",
                        "tipo": "Eléctrico",
                        "power": 40,
                        "accuracy": 100,
                        "pp": 30,
                        "generacion": "I",
                        "categoria": "Especial",
                        "efecto": "Parálisis",
                        "probabilidad_efecto": 10,
                    },
                    {
                        "id": 2,
                        "nombre": "Rayo",
                        "tipo": "Eléctrico",
                        "power": 90,
                        "accuracy": 100,
                        "pp": 15,
                        "generacion": "I",
                        "categoria": "Especial",
                        "efecto": "Parálisis",
                        "probabilidad_efecto": 10,
                    },
                ],
            },
            {
                "id": 6,
                "nombre": "Charizard",
                "naturaleza": {
                    "id": 2,
                    "nombre": "Audaz",
                    "aumenta_estadistica": "Ataque",
                    "reduce_estadistica": "Defensa",
                },
                "movimientos": [
                    {
                        "id": 3,
                        "nombre": "Llamarada",
                        "tipo": "Fuego",
                        "power": 110,
                        "accuracy": 85,
                        "pp": 5,
                        "generacion": "I",
                        "categoria": "Especial",
                        "efecto": "Quemadura",
                        "probabilidad_efecto": 30,
                    }
                ],
            },
            {
                "id": 9,
                "nombre": "Blastoise",
                "naturaleza": {
                    "id": 3,
                    "nombre": "Modesta",
                    "aumenta_estadistica": "Ataque Especial",
                    "reduce_estadistica": "Ataque",
                },
                "movimientos": [
                    {
                        "id": 4,
                        "nombre": "Hidrobomba",
                        "tipo": "Agua",
                        "power": 110,
                        "accuracy": 80,
                        "pp": 5,
                        "generacion": "I",
                        "categoria": "Especial",
                        "efecto": "Ninguno",
                        "probabilidad_efecto": None,
                    }
                ],
            },
            {
                "id": 3,
                "nombre": "Venusaur",
                "naturaleza": {
                    "id": 4,
                    "nombre": "Serena",
                    "aumenta_estadistica": "Defensa Especial",
                    "reduce_estadistica": "Ataque",
                },
                "movimientos": [
                    {
                        "id": 5,
                        "nombre": "Solar Rayo",
                        "tipo": "Planta",
                        "power": 120,
                        "accuracy": 100,
                        "pp": 10,
                        "generacion": "I",
                        "categoria": "Especial",
                        "efecto": "Ninguno",
                        "probabilidad_efecto": None,
                    }
                ],
            },
            {
                "id": 94,
                "nombre": "Gengar",
                "naturaleza": {
                    "id": 5,
                    "nombre": "Miedosa",
                    "aumenta_estadistica": "Velocidad",
                    "reduce_estadistica": "Defensa",
                },
                "movimientos": [
                    {
                        "id": 6,
                        "nombre": "Bola Sombra",
                        "tipo": "Fantasma",
                        "power": 80,
                        "accuracy": 100,
                        "pp": 15,
                        "generacion": "II",
                        "categoria": "Especial",
                        "efecto": "Ninguno",
                        "probabilidad_efecto": None,
                    }
                ],
            },
            {
                "id": 149,
                "nombre": "Dragonite",
                "naturaleza": {
                    "id": 6,
                    "nombre": "Firme",
                    "aumenta_estadistica": "Ataque",
                    "reduce_estadistica": "Defensa Especial",
                },
                "movimientos": [
                    {
                        "id": 7,
                        "nombre": "Puño Fuego",
                        "tipo": "Fuego",
                        "power": 100,
                        "accuracy": 100,
                        "pp": 15,
                        "generacion": "II",
                        "categoria": "Físico",
                        "efecto": "Ninguno",
                        "probabilidad_efecto": None,
                    }
                ],
            },
        ],
    }
    equipo_con_6_pokemons = {
        "id_equipo": 1,
        "nombre": "Equipo Elite",
        "pokemons_de_equipo": [
            {
                "id": 25,
                "nombre": "Pikachu",
                "naturaleza": {
                    "id": 1,
                    "nombre": "Activa",
                    "aumenta_estadistica": "Velocidad",
                    "reduce_estadistica": "Defensa",
                },
                "movimientos": [
                    {
                        "id": 1,
                        "nombre": "Impactrueno",
                        "tipo": "Eléctrico",
                        "power": 40,
                        "accuracy": 100,
                        "pp": 30,
                        "generacion": "I",
                        "categoria": "Especial",
                        "efecto": "Parálisis",
                        "probabilidad_efecto": 10,
                    },
                    {
                        "id": 2,
                        "nombre": "Rayo",
                        "tipo": "Eléctrico",
                        "power": 90,
                        "accuracy": 100,
                        "pp": 15,
                        "generacion": "I",
                        "categoria": "Especial",
                        "efecto": "Parálisis",
                        "probabilidad_efecto": 10,
                    },
                ],
            },
            {
                "id": 6,
                "nombre": "Charizard",
                "naturaleza": {
                    "id": 2,
                    "nombre": "Audaz",
                    "aumenta_estadistica": "Ataque",
                    "reduce_estadistica": "Defensa",
                },
                "movimientos": [
                    {
                        "id": 3,
                        "nombre": "Llamarada",
                        "tipo": "Fuego",
                        "power": 110,
                        "accuracy": 85,
                        "pp": 5,
                        "generacion": "I",
                        "categoria": "Especial",
                        "efecto": "Quemadura",
                        "probabilidad_efecto": 30,
                    }
                ],
            },
            {
                "id": 9,
                "nombre": "Blastoise",
                "naturaleza": {
                    "id": 3,
                    "nombre": "Modesta",
                    "aumenta_estadistica": "Ataque Especial",
                    "reduce_estadistica": "Ataque",
                },
                "movimientos": [
                    {
                        "id": 4,
                        "nombre": "Hidrobomba",
                        "tipo": "Agua",
                        "power": 110,
                        "accuracy": 80,
                        "pp": 5,
                        "generacion": "I",
                        "categoria": "Especial",
                        "efecto": "Ninguno",
                        "probabilidad_efecto": None,
                    }
                ],
            },
            {
                "id": 3,
                "nombre": "Venusaur",
                "naturaleza": {
                    "id": 4,
                    "nombre": "Serena",
                    "aumenta_estadistica": "Defensa Especial",
                    "reduce_estadistica": "Ataque",
                },
                "movimientos": [
                    {
                        "id": 5,
                        "nombre": "Solar Rayo",
                        "tipo": "Planta",
                        "power": 120,
                        "accuracy": 100,
                        "pp": 10,
                        "generacion": "I",
                        "categoria": "Especial",
                        "efecto": "Ninguno",
                        "probabilidad_efecto": None,
                    }
                ],
            },
            {
                "id": 94,
                "nombre": "Gengar",
                "naturaleza": {
                    "id": 5,
                    "nombre": "Miedosa",
                    "aumenta_estadistica": "Velocidad",
                    "reduce_estadistica": "Defensa",
                },
                "movimientos": [
                    {
                        "id": 6,
                        "nombre": "Bola Sombra",
                        "tipo": "Fantasma",
                        "power": 80,
                        "accuracy": 100,
                        "pp": 15,
                        "generacion": "II",
                        "categoria": "Especial",
                        "efecto": "Ninguno",
                        "probabilidad_efecto": None,
                    }
                ],
            },
            {
                "id": 149,
                "nombre": "Dragonite",
                "naturaleza": {
                    "id": 6,
                    "nombre": "Firme",
                    "aumenta_estadistica": "Ataque",
                    "reduce_estadistica": "Defensa Especial",
                },
                "movimientos": [
                    {
                        "id": 7,
                        "nombre": "Puño Fuego",
                        "tipo": "Fuego",
                        "power": 100,
                        "accuracy": 100,
                        "pp": 15,
                        "generacion": "II",
                        "categoria": "Físico",
                        "efecto": "Ninguno",
                        "probabilidad_efecto": None,
                    }
                ],
            },
        ],
    }
    teams.append(equipo_con_6_pokemons)

    response = client.post("/teams", json=equipo_mismo_id)

    assert response.status_code == 400
    assert response.json()["detail"] == "Ya existe un equipo con ese id"



def test_get_pokemon():
    response = client.get("/")
    assert response.status_code == 400
    assert response["id_equipo"] == 1

