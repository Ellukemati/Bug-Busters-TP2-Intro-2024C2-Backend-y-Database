from sqlmodel import SQLModel, Field, Relationship
from typing import List
from app.models.movimiento import Movimiento
from app.models.naturaleza import Naturaleza
class EquipoBase(SQLModel):
    nombre: str

class Equipo(EquipoBase, table=True):
    id_equipo: int = Field(primary_key=True)
    
    pokemons_de_equipo: list["Integrante_pokemon"] = Relationship(back_populates="equipo")

class EquipoPublic(EquipoBase):
    id_equipo: int
    nombre: str
    pokemons_de_equipo: list["Integrante_pokemonPublic"] = []


class IntegranteMovimientoLink(SQLModel, table=True):
    integrante_id: int = Field(foreign_key="integrante_pokemon.id", primary_key=True)
    movimiento_id: int = Field(foreign_key="movimiento.id", primary_key=True)


class Integrante_pokemonBase(SQLModel):
    pass
    
    


class Integrante_pokemon(Integrante_pokemonBase, table=True):
    id: int = Field(primary_key=True)
    equipo_id: int = Field(default=None, foreign_key="equipo.id_equipo")
    equipo: Equipo = Relationship(back_populates="pokemons_de_equipo")
    movimientos: list["Movimiento"] = Relationship(link_model=IntegranteMovimientoLink)
    pokemon_id: int = Field(foreign_key="pokemon.id")
    naturaleza_id: int = Field(foreign_key="naturaleza.id")
class Integrante_pokemonPublic(Integrante_pokemonBase):
    id: int
    pokemon_id: int
    naturaleza: Naturaleza
    movimientos: list["Movimiento"]