import unittest
from blackjack.player import Player

class TestPlayer(unittest.TestCase):
    def test_add_card(self):
        """Тест: Проверка добавления карты в руку игрока."""
        player = Player("Player")
        player.add_card("7_of_hearts")
        self.assertIn("7_of_hearts", player.hand)

    def test_get_score_without_ace(self):
        """Тест: Подсчет очков без учета туза."""
        player = Player("Player")
        player.add_card("10_of_hearts")
        player.add_card("9_of_diamonds")
        self.assertEqual(player.get_score(), 19)

    def test_get_score_with_ace(self):
        """Тест: Подсчет очков с учетом туза как 1 или 11."""
        player = Player("Player")
        player.add_card("ace_of_spades")
        player.add_card("8_of_diamonds")
        self.assertEqual(player.get_score(), 19)

        player.add_card("5_of_clubs")
        self.assertEqual(player.get_score(), 14)

    def test_bust(self):
        """Тест: Игрок превышает 21 очко."""
        player = Player("Player")
        player.add_card("10_of_hearts")
        player.add_card("queen_of_diamonds")
        player.add_card("5_of_clubs")
        self.assertGreater(player.get_score(), 21)
