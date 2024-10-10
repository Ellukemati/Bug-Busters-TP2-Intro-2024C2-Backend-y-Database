from pydantic import BaseModel
class Pokemon(BaseModel):
    num_indice: int
    nombre: str
    link_imagen: str
    tipo: str