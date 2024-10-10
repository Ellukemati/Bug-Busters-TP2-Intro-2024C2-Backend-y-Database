from fastapi import FastAPI
from routers.moves import router as moves_router
from routers.pokemons import router as pokemons_router
from routers.teams import router as teams_router

app = FastAPI()

app.include_router(moves_router, prefix="/moves", tags=["moves"])
app.include_router(pokemons_router, prefix="/pokemons", tags=["pokemons"])
app.include_router(teams_router, prefix="/teams", tags=["teams"])
