from fastapi import APIRouter
from app.routers.moves import router as moves_router
from app.routers.pokemons import router as pokemons_router
from app.routers.teams import router as teams_router

api_router = APIRouter()

api_router.include_router(moves_router, prefix="/moves", tags=["moves"])
api_router.include_router(pokemons_router, prefix="/pokemons", tags=["pokemons"])
api_router.include_router(teams_router, prefix="/teams", tags=["teams"])
