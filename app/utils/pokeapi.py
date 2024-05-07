'''interagir avec l'API PokeAPI et simuler des combats entre des Pokémon'''

import requests

BASE_URL = "https://pokeapi.co/api/v2"


def get_pokemon_name(api_id):
    """
        Get a pokemon name from the API pokeapi
    """
    return get_pokemon_data(api_id)['name']

def get_pokemon_stats(api_id):
    '''
        Get stats pokemon from the API pokeapi
    '''
    data = requests.get(f"{BASE_URL}/pokemon/{api_id}", timeout=10).json()
    return data.get("stats")

def get_pokemon_data(api_id):
    """
        Get data of pokemon name from the API pokeapi
    """
    return requests.get(f"{BASE_URL}/pokemon/{api_id}", timeout=10).json()

def battle_pokemon(first_api_id, second_api_id):
    """
        Do battle between 2 pokemons
    """
    premier_pokemon = get_pokemon_data(first_api_id)
    second_pokemon = get_pokemon_data(second_api_id)
    battle_result = battle_compare_stats\
        (get_pokemon_stats(first_api_id), get_pokemon_stats(second_api_id))
    if battle_result > 0:
        return premier_pokemon
    if battle_result < 0:
        return second_pokemon
    return {'winner': 'draw'}

def battle_compare_stats(first_pokemon_stats, second_pokemon_stats):
    """
        Compare given stat between two pokemons
    """
    battle_result = 0
    index = 0
    for stat in first_pokemon_stats:
        if stat['base_stat'] > second_pokemon_stats[index]['base_stat']:
            battle_result += 1
        elif stat['base_stat'] < second_pokemon_stats[index]['base_stat']:
            battle_result -= 1
        index += 1
    return battle_result
