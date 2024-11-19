import unittest
from tennis_game import TennisGame

class TestTennisGame(unittest.TestCase):
    def setUp(self):
        self.game = TennisGame("Saiteja", "Juluru")

    def create_score(self, player_one_points, player_two_points):
        for _ in range(player_one_points):
            self.game.player_one_scores()
        for _ in range(player_two_points):
            self.game.player_two_scores()

    def test_new_game_should_return_love_all(self):
        self.assertEqual(self.game.get_score(), "Love all")

    def test_player_one_wins_first_ball(self):
        self.game.player_one_scores()
        self.assertEqual(self.game.get_score(), "Fifteen,Love")

    def test_fifteen_all(self):
        self.game.player_one_scores()
        self.game.player_two_scores()
        self.assertEqual(self.game.get_score(), "Fifteen all")

    def test_player_two_wins_first_two_balls(self):
        self.create_score(0, 2)
        self.assertEqual(self.game.get_score(), "Love,Thirty")

    def test_player_one_wins_first_three_balls(self):
        self.create_score(3, 0)
        self.assertEqual(self.game.get_score(), "Forty,Love")

    def test_players_are_deuce(self):
        self.create_score(3, 3)
        self.assertEqual(self.game.get_score(), "Deuce")

    def test_player_one_wins_game(self):
        self.create_score(4, 0)
        self.assertEqual(self.game.get_score(), "Saiteja wins")

    def test_player_two_wins_game(self):
        self.create_score(1, 4)
        self.assertEqual(self.game.get_score(), "Juluru wins")

    def test_players_are_deuce_at_4(self):
        self.create_score(4, 4)
        self.assertEqual(self.game.get_score(), "Deuce")

    def test_player_two_advantage(self):
        self.create_score(4, 5)
        self.assertEqual(self.game.get_score(), "Advantage Juluru")

    def test_player_one_advantage(self):
        self.create_score(5, 4)
        self.assertEqual(self.game.get_score(), "Advantage Saiteja")

    def test_player_two_wins_after_advantage(self):
        self.create_score(6, 8)
        self.assertEqual(self.game.get_score(), "Juluru wins")

    def test_player_one_wins_after_advantage(self):
        self.create_score(8, 6)
        self.assertEqual(self.game.get_score(), "Saiteja wins")


if __name__ == "__main__":
    unittest.main()
