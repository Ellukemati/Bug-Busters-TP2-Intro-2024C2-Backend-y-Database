from sqlmodel import SQLModel, Field

class MovimientoBase(SQLModel):
    nombre: str
    tipo: str
    power: int | None = Field(default=None)
    accuracy: int | None = None
    pp: int
    generacion: str
    categoria: str
    efecto: str
    probabilidad_efecto: int | None = None


class Movimiento(MovimientoBase, table=True):
    id: int = Field(primary_key=True)