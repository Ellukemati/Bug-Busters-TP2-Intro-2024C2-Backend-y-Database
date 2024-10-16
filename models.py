from pydantic import BaseModel


class Pokemon(BaseModel):
    pokemon_id: int
    nombre: str
    imagen: str
    tipos: list[str]
    habilidades: list[str]
    altura: int
    peso: int
    estadisticas: dict[str, int]
    cadena_evolutiva: list[int]



class Naturaleza(BaseModel):
    id: int
    nombre: str
    aumenta_estadistica: str
    reduce_estadistica: str


class Movimiento(BaseModel):
    id: int
    nombre: str
    tipo: str
    power: int | None = None
    accuracy: int | None = None
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


class Error(BaseModel):
    detail: str

