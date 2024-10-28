# tests/test_main_menu.py

import pytest
import tkinter as tk
from gui.main_menu import MainMenu

@pytest.fixture
def root():
    root = tk.Tk()
    yield root
    root.destroy()

def test_main_menu_initialization(root):
    menu = MainMenu(root)

    play_vs_dealer_button = root.children.get("!button")
    play_vs_player_button = root.children.get("!button2")
    quit_button = root.children.get("!button3")

    assert play_vs_dealer_button is not None, "Start Game button not found"
    assert play_vs_player_button is not None, "Play vs Player button not found"
    assert quit_button is not None, "Quit button not found"
    assert play_vs_dealer_button.cget("text") == "Play vs Dealer", "Play vs Dealer button text mismatch"
    assert play_vs_player_button.cget("text") == "Player vs Player", "Player vs Player button text mismatch"
    assert quit_button.cget("text") == "Quit", "Quit button text mismatch"
