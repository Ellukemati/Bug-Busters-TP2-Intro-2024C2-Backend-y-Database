from sqlmodel import SQLModel, Field, Relationship
from app.models.movimiento import Movimiento

class Pokemon(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nombre: str
    url_imagen: str
    altura: int
    peso: int
    tipo_1: str
    tipo_2: str = Field(default=None)
    habilidad_1: str
    habilidad_2: str = Field(default=None)
    habilidad_3: str = Field(default=None)
    estadistica_hp: int
    estadistica_attack: int
    estadistica_defense: int
    estadistica_special_attack: int
    estadistica_special_defense: int
    estadistica_speed: int
    posibles_movimientos: list["PokemonMovimiento"] = Relationship(back_populates="pokemons")

class PokemonMovimiento(SQLModel, table=True):
    pokemon_id: int = Field(foreign_key="pokemon.id", primary_key=True)
    movimiento_id: int = Field(foreign_key="movimiento.id", primary_key=True)
    pokemon: Pokemon = Relationship(back_populates="posibles_movimientos")
    movimiento: Movimiento = Relationship(back_populates="pokemons")