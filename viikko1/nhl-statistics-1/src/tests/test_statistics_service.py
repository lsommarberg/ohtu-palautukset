import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_player_name_search(self):
        result = self.stats.search("Semenko")
        self.assertEqual(result.name, "Semenko")

    def test_search_non_existing_player(self):
        result = self.stats.search("Player")
        self.assertIsNone(result)

    def test_team_members(self):
        result = self.stats.team("EDM")
        self.assertEqual(len(result), 3)

    def test_top_negative(self):
        
        top_players = self.stats.top(-1)
        self.assertEqual(top_players, [])

    def test_top_player(self):
        result = self.stats.top(0)
        self.assertEqual(len(result), 1)
        