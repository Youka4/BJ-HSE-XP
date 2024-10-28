import unittest
from blackjack.deck import Deck

class TestDeck(unittest.TestCase):
    def test_deck_initialization(self):
        """Тест: Колода должна содержать 52 карты при инициализации."""
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)

    def test_deck_shuffling(self):
        """Тест: После тасования колода не должна быть в исходном порядке."""
        deck1 = Deck()
        deck2 = Deck()
        deck2.shuffle()
        self.assertNotEqual(deck1.cards, deck2.cards)

    def test_draw_card(self):
        """Тест: После вытягивания карты колода должна уменьшиться на 1 карту."""
        deck = Deck()
        initial_count = len(deck.cards)
        deck.draw_card()
        self.assertEqual(len(deck.cards), initial_count - 1)

    def test_empty_deck(self):
        """Тест: При вытягивании карты из пустой колоды должно возвращаться None."""
        deck = Deck()
        deck.cards = []
        self.assertIsNone(deck.draw_card())
