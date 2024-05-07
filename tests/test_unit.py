'''Unit Tests to Verify Combat results, stats compare, and data base intereractions'''

import unittest
import json
import sqlite3
from fastapi.testclient import TestClient
from app.utils.pokeapi import battle_compare_stats
from main import app


class TestCombatDraw(unittest.TestCase):
    '''
    Test Verify combat draw
    '''

    def setUp(self):
        self.client = TestClient(app)

    def test_getcombat_draw(self):
        ''' Test Verify combat draw '''
        test = self.client.get("pokemons/1&1")
        answer = json.loads(test.content)
        self.assertEqual(answer, {"winner" : "draw"})


class TestPokemonBattleSecondWin(unittest.TestCase):
    '''
    Test Combat PokeStats
    '''

    def test_battle_compare_stats(self):
        """test battle second pokemon win"""
        pokemon1_stats = [{"base_stat": 50}, {"base_stat": 60}, {"base_stat": 70}]
        pokemon2_stats = [{"base_stat": 60}, {"base_stat": 70}, {"base_stat": 80}]
        expected_result = -3
        result = battle_compare_stats(pokemon1_stats, pokemon2_stats)
        self.assertEqual(result, expected_result)

class TestPokemonBattleDraw(unittest.TestCase):
    '''
    Test Combat PokeStats
    '''

    def test_battle_compare_stats_draw(self):
        """test battle when draw"""
        pokemon1_stats = [{"base_stat": 50}, {"base_stat": 60}, {"base_stat": 70}]
        pokemon2_stats = [{"base_stat": 50}, {"base_stat": 60}, {"base_stat": 70}]
        expected_result = 0
        result = battle_compare_stats(pokemon1_stats, pokemon2_stats)
        self.assertEqual(result, expected_result)

class TestPokemonBattleFirstWin(unittest.TestCase):
    '''
    Test Combat PokeStats
    '''

    def test_battle_compare_stats_first_winner(self):
        """test battle first pokemon win"""
        pokemon1_stats = [{"base_stat": 60}, {"base_stat": 60}, {"base_stat": 70}]
        pokemon2_stats = [{"base_stat": 55}, {"base_stat": 60}, {"base_stat": 70}]
        expected_result = 1
        result = battle_compare_stats(pokemon1_stats, pokemon2_stats)
        self.assertEqual(result, expected_result)

class TestTrainersBdd(unittest.TestCase):
    """Test trainer bdd"""
    def test_obtenir_liste_dresseur(self):
        """Test trainer bdd"""
        connexion = sqlite3.connect('sqlite.db')
        curseur = connexion.cursor()
        curseur.execute('SELECT * FROM trainers')
        resultat = curseur.fetchall()
        connexion.close
        self.assertIsNotNone(resultat)

class TestPokemonsBdd(unittest.TestCase):
    """Test obtenir list dresseur"""
    def test_obtenir_liste_pokemons(self):
        """Test obtenir list dresseur"""
        connexion = sqlite3.connect('sqlite.db')
        curseur = connexion.cursor()

        curseur.execute('SELECT * FROM pokemons')
        resultat = curseur.fetchall()
        connexion.close
        self.assertIsInstance(resultat, list)

if __name__ == '__main__':
    unittest.main()
