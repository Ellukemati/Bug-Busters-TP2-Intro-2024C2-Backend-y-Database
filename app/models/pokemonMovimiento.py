from sqlmodel import SQLModel, Field

class PokemonMovimiento(SQLModel, table=True):
    pokemon_id: int | None = Field(nullable=False, primary_key=True, foreign_key="pokemon.id")
    movimiento_id: int | None = Field(nullable=False, foreign_key="movimiento.id", primary_key=True)
