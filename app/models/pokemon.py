from sqlmodel import SQLModel, Field, Relationship


class PokemonBase(SQLModel):
    nombre: str
    url_imagen: str
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
    altura: int
    peso: int

class Pokemon(PokemonBase, table=True):
    pokemon_id: int = Field(primary_key=True, foreign_key="integrante_pokemon.pokemon_id")