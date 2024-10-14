from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app
from app.routers.pokemons import Naturalezas, estadisticas
from models import Naturaleza

client = TestClient(app)

fake_stats = [
    {"id": "1", "identifier": "attack"},
    {"id": "2", "identifier": "defense"},
    {"id": "3", "identifier": "special-attack"},
    {"id": "4", "identifier": "special-defense"},
]

fake_natures = [
    {
        "id": "1",
        "identifier": "hardy",
        "increased_stat_id": "1",
        "decreased_stat_id": "1",
    },
    {
        "id": "2",
        "identifier": "bold",
        "increased_stat_id": "2",
        "decreased_stat_id": "1",
    },
    {
        "id": "3",
        "identifier": "modest",
        "increased_stat_id": "3",
        "decreased_stat_id": "1",
    },
]


def mock_load_csv(file):
    if "stats.csv" in file:
        return fake_stats
    elif "natures.csv" in file:
        return fake_natures
    return []


@patch("app.open", side_effect=mock_load_csv)
def test_get_natures(mock_csv):
    Naturalezas.clear()
    with patch("app.routers.pokemons.open", side_effect=mock_load_csv):
        with open("stats.csv", mode="r") as estadisticas_file:
            reader = fake_stats
            for row in reader:
                estadisticas[row["id"]] = row["identifier"]

        with open("natures.csv", mode="r") as naturalezas_file:
            reader = fake_natures
            for row in reader:
                id_aumenta = row["increased_stat_id"]
                id_disminuye = row["decreased_stat_id"]

                nombre_aumenta = estadisticas.get(id_aumenta)
                nombre_disminuye = estadisticas.get(id_disminuye)

                naturaleza = Naturaleza(
                    id=int(row["id"]),
                    nombre=row["identifier"],
                    aumenta_estadistica=nombre_aumenta,
                    reduce_estadistica=nombre_disminuye,
                )
                Naturalezas.append(naturaleza)
    response = client.get("/pokemons/natures")
    assert response.status_code == 200

    data = response.json()

    assert len(data) == 3

    assert data[0]["nombre"] == "hardy"
    assert data[0]["aumenta_estadistica"] == "attack"
    assert data[0]["reduce_estadistica"] == "attack"

    assert data[1]["nombre"] == "bold"
    assert data[1]["aumenta_estadistica"] == "defense"
    assert data[1]["reduce_estadistica"] == "attack"

    assert data[2]["nombre"] == "modest"
    assert data[2]["aumenta_estadistica"] == "special-attack"
    assert data[2]["reduce_estadistica"] == "attack"
