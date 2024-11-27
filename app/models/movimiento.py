from sqlmodel import SQLModel, Field, Relationship

from app.models.pokemonMovimiento import PokemonMovimiento
from app.models.IntegranteMovimientoLink import IntegranteMovimientoLink

class MovimientoBase(SQLModel):
    nombre: str
    tipo: str
    power: int | None = Field(default=None)
    accuracy: int | None = Field(default=None)
    pp: int | None = Field(default=None)
    generacion: str
    categoria: str
    efecto: str
    probabilidad_efecto: int | None = Field(default=None)

class Movimiento(MovimientoBase, table=True):
    id: int = Field(primary_key=True)
    pokemon_que_lo_aprenden: list["Pokemon"] = Relationship(back_populates="posibles_movimientos", link_model=PokemonMovimiento)
    integrante_que_aprendieron: list["Integrante_pokemon"] = Relationship(back_populates="movimientos", link_model=IntegranteMovimientoLink)

class MovimientoPublic(MovimientoBase):
    id: int = Field(primary_key=True)
    nombre: str
    tipo: str
    power: int | None = Field(default=None)
    accuracy: int | None = Field(default=None)
    pp: int | None = Field(default=None)
    generacion: str
    categoria: str
    efecto: str
    probabilidad_efecto: int | None = Field(default=None)