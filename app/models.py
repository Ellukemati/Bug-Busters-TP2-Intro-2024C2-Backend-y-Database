from pydantic import BaseModel


class Pokemon(BaseModel):
    id: int
    nombre: str
    imagen: str
    tipo: str


class Equipo(BaseModel):
    id_equipo: int
    nombre: str
    pokemons_de_equipo: list[Pokemon]
