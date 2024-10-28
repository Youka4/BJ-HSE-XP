The project applies Extreme Programming (XP) practices such as frequent releases and Test-Driven Development (TDD) to ensure high code quality and user-friendly design.

---

## Core Features

1. **Single Player Mode**: 
   - User plays against the dealer, who follows basic Blackjack rules.
   - The dealer (bot) makes moves automatically based on its current hand.

2. **Two Player Mode**:
   - Two players take turns playing on the same device.
   - Players alternate turns: each player can hit (take a card) or stand (stop taking cards).

3. **Simple Controls**:
   - Players interact with the game via "Hit" and "Stand" buttons.
   - The current score and game status (win, lose, or bust) are displayed.

4. **Automatic Score Calculation**:
   - The game automatically calculates each player's score.
   - The end of each game round shows the winner, loser, or if it’s a draw.

5. **Game Restart Option**:
   - Players can restart the game after completing a round.

---

## Interface Requirements

1. **Main Menu**:
   - Provides options to start a "Single Player" game or "Two Player" game.

2. **Game Window**:
   - A simple window displays each player’s cards and current score.
   - Includes "Hit" and "Stand" buttons for player actions.
   - Shows game result notifications such as "You Win," "Dealer Wins," or "Draw."

3. **Messages and Notifications**:
   - Displays game information: "Your Turn," "Dealer's Turn," "You Win," "Dealer Wins," etc.
   - Shows error messages for invalid actions, if any.

4. **Restart Button**:
   - Allows players to restart the game quickly from the game window.

---

## User Tests

1. **Game Mode Selection Test**:
   - Verify that users can choose between "Single Player" and "Two Player" modes.

2. **Hit and Stand Actions Test**:
   - Confirm that the player can hit (draw a card) and see the updated score, or stand (end their turn) correctly.

3. **Win Condition Test**:
   - Ensure the application correctly identifies the winner if a player reaches 21 or goes bust (exceeds 21).

---

This file describes the goals, main features, and interface requirements of the Blackjack application, along with basic user tests to ensure game functionality and correctness.