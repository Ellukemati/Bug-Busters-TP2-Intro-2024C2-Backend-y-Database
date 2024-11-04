from sqlmodel import SQLModel, Field, Relationship
from models import Integrante_pokemon
class EquipoBase(SQLModel):
    nombre: str
    pokemons_de_equipo: list["Integrante_pokemon"] = Relationship(back_populates="Integrante_pokemon")

class Equipo(EquipoBase, table=True):
    id_equipo: int = Field(primary_key=True)

class EquipoPublic(EquipoBase):
    id_equipo: int
    nombre: str
    pokemons: list["Integrante_pokemon"] = []