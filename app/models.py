from pydantic import BaseModel


class Movimiento(BaseModel):
    id: int | None = None
    nombre: str | None = None
    tipo: str | None = None
    power: int | None = None
    accuracy: int | None = None
    pp: int | None = None
    generacion: str | None = None
    categoria: str | None = None
    efecto: str | None = None


class Error(BaseModel):
    detail: str
