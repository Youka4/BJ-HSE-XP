# Code Structure for "Blackjack Desktop Game"

## Overview
The codebase for the Blackjack desktop game is organized to separate concerns between game logic, graphical interface (GUI), testing, and documentation. This modular structure improves maintainability, readability, and facilitates testing, following good software engineering practices and XP principles.

---

## Code Structure

### 1. Root Directory
The root directory of the repository contains:
- `README.md`: Project overview, installation instructions, and a quick start guide.
- `requirements.txt`: Lists required libraries and dependencies for easy setup.
- `main.py`: Entry point to launch the application.
- `docs/`: Documentation folder, which includes a description of the project and detailed explanations for installation, features, and usage.

### 2. Directory Structure

The main code and assets are organized into specific directories:

```plaintext
.
├── blackjack/
│   ├── __init__.py
│   ├── game.py           # Core game logic (player actions, scoring, and game rules)
│   ├── player.py         # Defines Player and Dealer classes with attributes and behaviors
│   ├── deck.py           # Contains logic for the deck of cards, shuffling, and dealing
│   └── bot.py            # Dealer (bot) AI logic
│
├── gui/
│   ├── __init__.py
│   ├── gui_manager.py    # Manages the main window, menus, and transitions between screens
│   ├── game_screen.py    # Main game screen with buttons and displays for scores and cards
│   ├── main_menu.py      # Initial screen for selecting game mode (single-player or multiplayer)
│   └── components.py     # Custom components like buttons, labels, and card representations
│
├── tests/
│   ├── __init__.py
│   ├── test_game.py      # Unit tests for core game logic and rules
│   ├── test_bot.py       # Tests for dealer (bot) behavior and decision-making
│   ├── test_player.py    # Tests for Player and Dealer class functionality
│   └── test_gui.py       # Tests for GUI components and user interaction
│
├── assets/
│   ├── images/           # Images for card faces and background
│   └── fonts/            # Fonts for custom text styling
│    
│
└── docs/
    └── *.md              # Documentation files with detailed descriptions, use cases, and examples
