from pydantic import BaseModel

class Movimiento(BaseModel):
    id: int | None = None
    nombre: str | None = None
    tipo: str | None = None
    power: int | None = None
    accuracy: int | None = None
    pp: int | None = None
    generacion: str | None = None
    categoria: str | None = None
    efecto: str | None = None

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
    
class Integrante_pokemon(BaseModel):
    id: int
    nombre: str
    naturaleza: Naturaleza
    movimientos: list[Movimiento]

class Equipo(BaseModel):
    id_equipo: int
    nombre: str
    pokemons_de_equipo: list[Integrante_pokemon]