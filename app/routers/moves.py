from fastapi import APIRouter, HTTPException, status
import csv
from models import Error
from app.models.pokemon import Pokemon
from app.models.movimiento import Movimiento
from app.routers.funciones import buscar_movimiento

router = APIRouter()

MOVES_CSV = "moves.csv"
MOVES_DAMAGE_CSV = "move_damage_class.csv"
MOVE_EFFECT_CSV = "move_effect.csv"
TYPE_NAMES = "type_names.csv"
ESPANIOL = 7
INGLES = 9


