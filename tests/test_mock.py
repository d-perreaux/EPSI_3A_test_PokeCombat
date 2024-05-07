'''Tests Mock Verify Get NamePokemon, Trainer items are in a list, get CombatStats'''

import unittest
import sys
import os
from unittest.mock import patch
from app.utils import pokeapi
from app.routers.trainers import get_trainers
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, project_root)


class TestPokeAPIUtils(unittest.TestCase):
    '''
    Verify API pokemon = Name PokemonId
    '''

    @patch('app.utils.pokeapi.requests.get')
    def test_get_pokemon_name(self, mock_get):
        """Test pokemon name"""
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {"name": "Pikachu"}
        pokemon_name = pokeapi.get_pokemon_name(25)
        self.assertEqual(pokemon_name, "Pikachu")

class TestTrainerRouter(unittest.TestCase):
    '''
    Verify Trainer Router
    '''

    @patch('app.routers.trainers.actions.get_trainers')
    def test_get_trainers_inventory_response_is_list(self, mock_get_trainers):
        """Test get trainers response"""
        mock_response = mock_get_trainers.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"name": "Dimitri", "birthdate": "2024-01-11",\
              "id": 1, "inventory": [], "pokemons": []},
            {"name": "Jeremie", "birthdate": "2024-02-11",\
              "id": 2, "inventory": [], "pokemons": []},
            {"name": "Thibault", "birthdate": "2024-03-11",\
              "id": 3, "inventory": [], "pokemons": []}
        ]
        resp = get_trainers()
        for trainer in resp:
            self.assertIsInstance(trainer['inventory'], list)

class TestPokeAPIGetStats(unittest.TestCase):
    '''
    Verify API pokemon = get stats
    '''

    @patch('app.utils.pokeapi.requests.get')
    def test_get_pokemon_stats(self, mock_get):
        """Test pokemon stats"""
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        stats = [{"base_stat":45,"effort":0,"stat":\
                  {"name":"hp","url":"https://pokeapi.co/api/v2/stat/1/"}},\
                    {"base_stat":49,"effort":0,"stat":{"name":"attack",\
                    "url":"https://pokeapi.co/api/v2/stat/2/"}},\
                      {"base_stat":49,"effort":0,"stat":\
                    {"name":"defense","url":"https://pokeapi.co/api/v2/stat/3/"}},\
                      {"base_stat":65,"effort":1,"stat":{"name":"special-attack","url":\
                      "https://pokeapi.co/api/v2/stat/4/"}},\
                        {"base_stat":65,"effort":0,"stat":\
                      {"name":"special-defense","url":"https://pokeapi.co/api/v2/stat/5/"}},\
                        {"base_stat":45,"effort":0,"stat":\
                         {"name":"speed","url":"https://pokeapi.co/api/v2/stat/6/"}}]
        mock_response.json.return_value = \
          {"stats": [{"base_stat":45,"effort":0,"stat":\
                      {"name":"hp","url":"https://pokeapi.co/api/v2/stat/1/"}},\
                        {"base_stat":49,"effort":0,"stat":{"name":"attack","url":"https://pokeapi.co/api/v2/stat/2/"}},\
                          {"base_stat":49,"effort":0,"stat":{"name":"defense","url":"https://pokeapi.co/api/v2/stat/3/"}},\
                            {"base_stat":65,"effort":1,"stat":{"name":"special-attack","url":"https://pokeapi.co/api/v2/stat/4/"}},\
                              {"base_stat":65,"effort":0,"stat":{"name":"special-defense","url":"https://pokeapi.co/api/v2/stat/5/"}},\
                                {"base_stat":45,"effort":0,"stat":{"name":"speed","url":"https://pokeapi.co/api/v2/stat/6/"}}]}
        pokemon_name = pokeapi.get_pokemon_stats(1)
        self.assertEqual(pokemon_name, stats)

if __name__ == '__main__':
    unittest.main()
