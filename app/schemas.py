'''Schémas Pydantic qui servent à valider et à désérialiser les données'''

from datetime import date
from typing import  List, Optional, Union
from pydantic import BaseModel

#
#  ITEM
#
class ItemBase(BaseModel): # pylint: disable=too-few-public-methods
    '''Item définit par les champs name et description'''
    name: str
    description: Union[str, None] = None

class ItemCreate(ItemBase): # pylint: disable=too-few-public-methods
    '''Créer un nouvel item hérité de ItemBase'''


class Item(ItemBase): # pylint: disable=too-few-public-methods
    '''Ajout des champs id et trainer id et config de l'item sur l'ORM pour serialization'''
    id: int
    trainer_id: int

    class Config: # pylint: disable=too-few-public-methods
        '''sérialiser/désérialiser des objets SQLAlchemy.'''
        orm_mode = True

#
#  POKEMON
#
class PokemonBase(BaseModel): # pylint: disable=too-few-public-methods
    '''Schéma de base pour un Pokémon. Il définit les champs api_id et custom_name.'''
    api_id: int
    custom_name: Optional[str] = None

class PokemonCreate(PokemonBase): # pylint: disable=too-few-public-methods
    '''Schéma utilisé pour créer un nouveau Pokémon. Il hérite de PokemonBase'''


class Pokemon(PokemonBase): # pylint: disable=too-few-public-methods
    '''Schéma complet pour un Pokémon.'''
    id: int
    name: str
    trainer_id: int

    class Config: # pylint: disable=too-few-public-methods
        '''sérialiser/désérialiser des objets SQLAlchemy.'''
        orm_mode = True
#
#  TRAINER
#
class TrainerBase(BaseModel): # pylint: disable=too-few-public-methods
    '''Schéma de base pour un dresseur. Il définit les champs name et birthdate.'''
    name: str
    birthdate: date

class TrainerCreate(TrainerBase): # pylint: disable=too-few-public-methods
    ''' Schéma utilisé pour créer un nouveau dresseur. Il hérite de TrainerBase'''


class Trainer(TrainerBase): # pylint: disable=too-few-public-methods
    '''Schéma complet pour un dresseur'''
    id: int
    inventory: List[Item] = []
    pokemons: List[Pokemon] = []

    class Config: # pylint: disable=too-few-public-methods
        '''sérialiser/désérialiser des objets SQLAlchemy.'''
        orm_mode = True
