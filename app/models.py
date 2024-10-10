from pydantic import BaseModel


class Pokemon(BaseModel):
    id: int
    nombre: str
    imagen: str
    tipo: str
