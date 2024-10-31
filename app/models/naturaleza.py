from sqlmodel import SQLModel, Field

class NaturalezaBase(SQLModel):
    nombre: str
    aumenta_estadistica: str
    reduce_estadistica: str

class Naturaleza(NaturalezaBase, table=True):
    id: int = Field(primary_key=True)

class NaturalezaCreate(NaturalezaBase):
    pass