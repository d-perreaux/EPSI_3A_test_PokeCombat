'''gérer les requêtes relatives aux Pokémon'''

from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter,  Depends
from app import actions, schemas
from app.utils.utils import get_db
from app.utils.pokeapi import battle_pokemon

router = APIRouter()


@router.get("/", response_model=List[schemas.Pokemon])
def get_pokemons(skip: int = 0, limit: int = 100, database: Session = Depends(get_db)):
    """
        Return all pokemons
        Default limit is 100
    """
    pokemons = actions.get_pokemons(database, skip=skip, limit=limit)
    return pokemons

@router.get("/{poke1_id}&{poke2_id}")
def get_pokemon_fight_result(poke1_id: int, poke2_id: int, database: Session = Depends(get_db)):
    '''simuler un combat entre les deux Pokémon'''
    return battle_pokemon(poke1_id, poke2_id)
