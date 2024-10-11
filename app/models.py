from pydantic import BaseModel

class Pokemon(BaseModel):
    id: int
    nombre: str
    imagen: str
    tipos: list[str]
    habilidades: list[str]
    altura: int
    peso: int
    estadisticas: dict[str, int]