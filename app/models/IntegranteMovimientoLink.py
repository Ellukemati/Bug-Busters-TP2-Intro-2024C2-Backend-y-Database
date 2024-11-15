from sqlmodel import SQLModel, Field


class IntegranteMovimientoLink(SQLModel, table=True):
    integrante_id: int = Field(foreign_key="integrante_pokemon.id", primary_key=True)
    movimiento_id: int = Field(foreign_key="movimiento.id", primary_key=True)
