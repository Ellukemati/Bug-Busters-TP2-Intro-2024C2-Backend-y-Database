from sqlmodel import SQLModel, Field, Relationship
from typing import List
from app.models.Integrante_pokemon import Integrante_pokemon
class EquipoBase(SQLModel):
    nombre: str
    

class Equipo(EquipoBase, table=True):
    id_equipo: int = Field(primary_key=True)
    pokemons_de_equipo: list["Integrante_pokemon"] = Relationship(back_populates="equipo")

class EquipoPublic(EquipoBase):
    id_equipo: int
    nombre: str
    pokemons: list["Integrante_pokemon"] = []