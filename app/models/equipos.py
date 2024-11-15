from sqlmodel import SQLModel, Field, Relationship
from typing import List
from app.models.movimiento import Movimiento, MovimientoPublic
from app.models.naturaleza import Naturaleza
from app.models.IntegranteMovimientoLink import IntegranteMovimientoLink
class EquipoBase(SQLModel):
    nombre: str

class Equipo(EquipoBase, table=True):
    id_equipo: int = Field(primary_key=True)
    
    pokemons_de_equipo: list["Integrante_pokemon"] = Relationship(back_populates="equipo")

class EquipoPublic(EquipoBase):
    id_equipo: int
    nombre: str
    pokemons_de_equipo: list["Integrante_pokemonPublic"] 
class EquipoCreate(EquipoBase):
    id_equipo: int
    nombre:str
    pokemons_de_equipo: list["Integrante_pokemonCreate"]



class Integrante_pokemonBase(SQLModel):
    pass
    
    


class Integrante_pokemon(Integrante_pokemonBase, table=True):
    id: int = Field(primary_key=True)
    equipo_id: int = Field(default=None, foreign_key="equipo.id_equipo")
    naturaleza: str
    equipo: Equipo = Relationship(back_populates="pokemons_de_equipo")
    movimientos: list[Movimiento] = Relationship(back_populates="integrante_que_aprendieron",link_model=IntegranteMovimientoLink)
    pokemon_id: int = Field(foreign_key="pokemon.id")
    naturaleza_id: int = Field(foreign_key="naturaleza.id")
class Integrante_pokemonCreate(Integrante_pokemonBase):
    id:int
    equipo_id: int
    pokemon_id: int
    naturaleza_id: int
    movimientos_ids: list[int]
class Integrante_pokemonPublic(Integrante_pokemonBase):
    pokemon_id: int
    naturaleza: str
    movimientos: list["MovimientoPublic"]