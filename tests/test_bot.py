import pytest
from blackjack.bot import DealerBot
from blackjack.deck import Deck
from blackjack.player import Player

def test_dealer_decide_hit():
    """Тест: дилер решает взять карту, если его счет меньше 17."""
    dealer = DealerBot()

    dealer.hand = ["2_of_hearts", "5_of_diamonds"]
    assert dealer.decide_hit() is True

    dealer.hand = ["10_of_clubs", "5_of_spades"]
    assert dealer.decide_hit() is True

    dealer.hand = ["10_of_clubs", "7_of_diamonds"]
    assert dealer.decide_hit() is False

def test_dealer_stand_decision():
    """Тест: дилер останавливается, если его счет 17 или выше."""
    dealer = DealerBot()

    dealer.hand = ["10_of_hearts", "7_of_spades"]
    assert dealer.decide_hit() is False

    dealer.hand = ["10_of_hearts", "8_of_spades"]
    assert dealer.decide_hit() is False

def test_dealer_bust():
    """Тест: проверка, что дилер корректно распознает превышение счета (больше 21)."""
    dealer = DealerBot()

    dealer.hand = ["10_of_hearts", "8_of_spades", "5_of_diamonds"]
    assert dealer.get_score() > 21
