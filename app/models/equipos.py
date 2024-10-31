from sqlmodel import SQLModel, Field
from models import Integrante_pokemon
class EquipoBase(SQLModel):
    nombre: str
    pokemons_de_equipo: list[Integrante_pokemon]

class Equipo(EquipoBase, table=True):
    id_equipo: int = Field(primary_key=True)