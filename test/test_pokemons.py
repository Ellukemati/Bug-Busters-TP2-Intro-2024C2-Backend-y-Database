from fastapi.testclient import TestClient
from app.routers.pokemons import POKEMON_DATA
from app.models.pokemon import Pokemon
from app.models.naturaleza import Naturaleza
from main import app
from test.jsons import nature_1, nature_2, nature_3, infernape_mock, movimientos_infernape
import pytest

client = TestClient(app)


