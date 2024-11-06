from sqlmodel import SQLModel, Field, Relationship
from app.models.movimiento import Movimiento
from app.models.naturaleza import Naturaleza
from app.models.equipos import Equipo
from typing import List

class IntegranteMovimientoLink(SQLModel):
    integrante_id: int = Field(foreign_key="integrante_pokemon.id", primary_key=True)
    movimiento_id: int = Field(foreign_key="Movimiento.id", primary_key=True)


class Integrante_pokemonBase(SQLModel):
    pokemon_id: int = Field(foreign_key="pokemon.pokemon.id")
    naturaleza_id: int = Field(foreign_key="Naturaleza.id")
    
    pokemon = Relationship()
    naturaleza = Relationship()
    movimientos: List[Movimiento] = Relationship(link_model="IntegranteMovimientoLink")


class Integrante_pokemon(Integrante_pokemonBase, table=True):
    id: int = Field(primary_key=True)
    equipo_id: int = Field(default=None, foreign_key="Equipo.id_equipo")
    equipo: Equipo = Relationship(back_populates="pokemons_de_equipo")

class Integrante_pokemonPublic(Integrante_pokemonBase):
    pokemon_id: int
    nombre: str
    naturaleza: Naturaleza
    movimientos: List[Movimiento] = []
