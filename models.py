from pydantic import BaseModel


class Pokemon(BaseModel):
    id: int
    nombre: str
    imagen: str
    tipo: str


class Naturaleza(BaseModel):
    id: int
    nombre: str
    aumenta_estadistica: str
    reduce_estadistica: str


class Movimiento(BaseModel):
    id: int
    nombre: str
    tipo: str
    power: int
    accuracy: int
    pp: int
    generacion: str
    categoria: str
    efecto: str
    probabilidad_efecto: int | None = None


class Integrante_pokemon(BaseModel):
    id: int
    nombre: str
    naturaleza: Naturaleza
    movimientos: list[Movimiento]


class Equipo(BaseModel):
    id_equipo: int
    nombre: str
    pokemons_de_equipo: list[Integrante_pokemon]
