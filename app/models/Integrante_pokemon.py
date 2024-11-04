from sqlmodel import SQLModel, Field, Relationship
from app.models.movimiento import Movimiento
from app.models.naturaleza import Naturaleza


class IntegranteMovimientoLink(SQLModel):
    integrante_id: int = Field(foreign_key="integrante_pokemon.id", primary_key=True)
    movimiento_id: int = Field(foreign_key="Movimiento.id", primary_key=True)


class Integrante_pokemonBase(SQLModel):
    pokemon_id: int = Field(foreign_key="pokemon.pokemon.id")
    naturaleza_id: int = Field(foreign_key="Naturaleza.id")
    equipo_id: int = Field(default=None, foreign_key="Equipo.id_equipo")
    equipo = Relationship(back_populates="integrantes")
    pokemon = Relationship()
    naturaleza = Relationship()
    movimientos: list["Movimiento"] = Relationship(link_model=IntegranteMovimientoLink)


class Integrante_pokemon(Integrante_pokemonBase, table=True):
    id: int = Field(primary_key=True)

class Integrante_pokemonPublic(Integrante_pokemonBase):
    pokemon_id: int
    nombre: str
    naturaleza: Naturaleza
    movimientos: list["Movimiento"] = []