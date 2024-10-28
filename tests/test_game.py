import unittest
from blackjack.game import BlackjackGame

class TestBlackjackGame(unittest.TestCase):
    def setUp(self):
        """Инициализация новой игры перед каждым тестом."""
        self.game = BlackjackGame()

    def test_initial_deal(self):
        """Тест: У игрока и дилера должно быть по две карты в начале игры."""
        self.game.start_game()
        self.assertEqual(len(self.game.player.hand), 2)
        self.assertEqual(len(self.game.dealer.hand), 2)

    def test_player_hit(self):
        """Тест: После взятия карты игрока у него должно быть три карты."""
        self.game.start_game()
        self.game.player_hit()
        self.assertEqual(len(self.game.player.hand), 3)

    def test_dealer_turn(self):
        """Тест: Дилер должен продолжать брать карты, пока у него менее 17 очков."""
        self.game.start_game()
        self.game.dealer_turn()
        self.assertGreaterEqual(self.game.dealer.get_score(), 17)

    def test_check_winner_player_wins(self):
        """Тест: Проверка победы игрока, если у него больше очков, чем у дилера."""
        self.game.player.add_card("10_of_hearts")
        self.game.player.add_card("9_of_diamonds")
        self.game.dealer.add_card("8_of_clubs")
        self.game.dealer.add_card("7_of_spades")
        self.game.check_winner()
        self.assertTrue(self.game.game_over)

    def test_check_winner_dealer_wins(self):
        """Тест: Проверка победы дилера, если у игрока перебор."""
        self.game.player.add_card("10_of_hearts")
        self.game.player.add_card("9_of_diamonds")
        self.game.player.add_card("5_of_clubs")
        self.game.check_winner()
        self.assertTrue(self.game.game_over)
