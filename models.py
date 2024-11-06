from pydantic import BaseModel 
from sqlmodel import SQLModel, Field, Relationship

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

class NaturalezaBase(SQLModel):
    nombre: str
    aumenta_estadistica: str
    reduce_estadistica: str

class Naturaleza(NaturalezaBase, table=True):
    id: int = Field(primary_key=True) 

class NaturalezaPublic(NaturalezaBase):
    id: int
    nombre: str
    aumenta_estadistica: str
    reduce_estadistica: str

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
    pokemon_id: int = Field(primary_key=True)
    

class EquipoBase(SQLModel):
    nombre: str

class Equipo(EquipoBase, table=True):
    id_equipo: int = Field(primary_key=True)
    pokemons_de_equipo: list["Integrante_pokemon"] = Relationship(back_populates="equipo")

class EquipoPublic(EquipoBase):
    id_equipo: int
    nombre: str
    pokemons: list["Integrante_pokemon"] = []

class IntegranteMovimientoLink(SQLModel):
    integrante_id: int = Field(foreign_key="integrante_pokemon.id", primary_key=True)
    movimiento_id: int = Field(foreign_key="Movimiento.id", primary_key=True)


class Integrante_pokemonBase(SQLModel):
    pokemon_id: int = Field(foreign_key="pokemon.pokemon.id")
    naturaleza_id: int = Field(foreign_key="Naturaleza.id")
    
    


class Integrante_pokemon(Integrante_pokemonBase, table=True):
    id: int = Field(primary_key=True)
    equipo_id: int = Field(default=None, foreign_key="Equipo.id_equipo")
    equipo: Equipo = Relationship(back_populates="pokemons_de_equipo")
    movimientos: list["Movimiento"] = Relationship(link_model="IntegranteMovimientoLink")
class Integrante_pokemonPublic(Integrante_pokemonBase):
    pokemon_id: int
    naturaleza: Naturaleza
    movimientos: list["Movimiento"] = []





class Error(BaseModel):
    detail: str

