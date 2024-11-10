from sqlmodel import SQLModel, Field

class NaturalezaBase(SQLModel):
    nombre: str
    aumenta_estadistica: str
    reduce_estadistica: str

class Naturaleza(NaturalezaBase, table=True):
    id: int = Field(primary_key=True, foreign_key="integrante_pokemon.naturaleza_id") 

class NaturalezaPublic(NaturalezaBase):
    id: int
    nombre: str
    aumenta_estadistica: str
    reduce_estadistica: str