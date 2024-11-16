from sqlmodel import SQLModel, Field, Relationship
from app.models.pokemonMovimiento import PokemonMovimiento
from app.models.movimiento import Movimiento

class PokemonBase(SQLModel):
    nombre: str
    url_imagen: str
    altura: int
    peso: int
    tipo_1: str
    tipo_2: str = Field(default=None, nullable=True)
    habilidad_1: str
    habilidad_2: str = Field(default=None, nullable=True)
    habilidad_3: str = Field(default=None, nullable=True)
    estadistica_hp: int
    estadistica_attack: int
    estadistica_defense: int
    estadistica_special_attack: int
    estadistica_special_defense: int
    estadistica_speed: int
    id_evolucion_anterior: int = Field(default=None, nullable=True)
    id_evolucion_siguiente: int = Field(default=None, nullable=True)


class Pokemon(PokemonBase, table=True):
    id: int = Field(primary_key=True)
    posibles_movimientos: list["Movimiento"] = Relationship(back_populates="pokemon_que_lo_aprenden", link_model=PokemonMovimiento)

