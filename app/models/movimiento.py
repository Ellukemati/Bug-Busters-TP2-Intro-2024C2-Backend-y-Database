from sqlmodel import SQLModel, Field, Relationship

from app.models.pokemonMovimiento import PokemonMovimiento

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
