from pydantic import BaseModel 
from app.models.movimiento import Movimiento 


class Pokemon(BaseModel):
    pokemon_id: int
    nombre: str
    imagen: str
    tipos: list[str]
    habilidades: list[str]
    movimientos_ids: list[int]
    altura: int
    peso: int
    estadisticas: dict[str, int]
    cadena_evolutiva_ids: list[int]


class Naturaleza(BaseModel):
    id: int
    nombre: str
    aumenta_estadistica: str
    reduce_estadistica: str


class Integrante_pokemon(BaseModel):
    id: int
    nombre: str
    naturaleza: Naturaleza
    movimientos: list[Movimiento]


class Equipo(BaseModel):
    id_equipo: int
    nombre: str
    pokemons_de_equipo: list[Integrante_pokemon]


class Error(BaseModel):
    detail: str
