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


class Naturaleza(BaseModel):
    id: int
    nombre: str
    aumenta_estadistica: str
    reduce_estadistica: str
