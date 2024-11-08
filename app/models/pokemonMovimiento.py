from sqlmodel import SQLModel, Field

class PokemonMovimiento(SQLModel, table=True):
    pokemon_id: int | None = Field(nullable=False, foreign_key="pokemon.id", primary_key=True)
    movimiento_id: int | None = Field(nullable=False, foreign_key="movimiento.id", primary_key=True)
