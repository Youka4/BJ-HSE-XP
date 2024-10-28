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
    menu = MainMenu(root, start_game_callback=lambda: None)

    start_button = root.children.get("!button")
    quit_button = root.children.get("!button2")

    assert start_button is not None, "Start Game button not found"
    assert quit_button is not None, "Quit button not found"
    assert start_button.cget("text") == "Start Game", "Start Game button text mismatch"
    assert quit_button.cget("text") == "Quit", "Quit button text mismatch"
