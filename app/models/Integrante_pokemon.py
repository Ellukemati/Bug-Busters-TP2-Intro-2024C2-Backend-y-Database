from sqlmodel import SQLModel, Field, Relationship
from app.models.movimiento import Movimiento


class IntegranteMovimientoLink(SQLModel):
    integrante_id: int
    movimiento_id: int


class Integrante_pokemonBase(SQLModel):
    pokemon_id: int = Field(foreign_key="pokemon.pokemon.id")
    naturaleza_id: int = Field(foreign_key="Naturaleza.id")

    equipo = Relationship(back_populates="integrantes")
    pokemon = Relationship()
    naturaleza = Relationship()
    movimientos: list[Movimiento] = Relationship(
        back_populates="integrantes", link_model=IntegranteMovimientoLink
    )


class Integrante_pokemon(Integrante_pokemonBase, table=True):
    id: int = Field(primary_key=True)
