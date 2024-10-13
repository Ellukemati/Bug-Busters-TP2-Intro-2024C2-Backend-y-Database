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
