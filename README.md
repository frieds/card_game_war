# War Card Game

This repository contains the implementation of the classic War card game in Python. The game is played by two players using a standard 52-card deck.

## How to Play

To play the game, run the `play_war_game.py` script. You will be prompted to enter the names of the two players. The game will then start, with each round requiring user input (pressing Enter) to proceed. The script will display the cards drawn by each player in every round and the winner of each round. The game continues until one of the players runs out of cards, at which point the script will display the name of the winning player.

## Game Rules

- The deck is divided evenly among the two players, giving each player a stack of 26 cards.
- Each round, both players reveal the top card of their stack.
- The player with the higher card wins the round and collects both cards, placing them at the bottom of their stack.
- If both players reveal a card of the same value, a "war" occurs. Each player then places up to four additional cards on the table, with last card being face-up. The player with the higher face-up card wins all the cards on the table.
- If another tie occurs, the process repeats until one player wins the round.
- The game continues until one player has all 52 cards or one player is holding no cards because it's a consecutive "war" tie, at which point the former player is declared the winner.

## Getting Started

### Prerequisites

The War card game implementation requires Python 3.6 or later.

### Running the Game

1. Clone the repository:

```
git clone git@github.com:frieds/card_game_war.git
```

2. Change to the repository directory:

```
cd card_game_war
```

3. Run the game:

```
python play_war_game.py
```

## Code Structure

The implementation is divided into the following classes:

- `CardValue`: An enumeration representing the value of each card.
- `Deck`: Represents a deck of cards and provides methods for shuffling and cutting the deck.
- `Player`: Represents a player in the game and provides methods for drawing cards, adding cards to their stack, and checking if they have cards left.
- `WarGame`: Represents the game itself and provides methods for playing rounds and determining the winner.

## Contributing

If you'd like to contribute to this project, please submit a pull request with your proposed changes. I welcome improvements and suggestions.

Here's a recommended workflow for contributors who want to set up the project with a virtual environment:

1. Clone the repository and navigate to the project's root directory.

2. Create a virtual environment using `venv`:

   ```
   python -m venv venv
   ```

   This will create a virtual environment in a folder named `venv` within your project directory.

3. Activate the virtual environment:

   - On Windows:
     ```
     .\venv\Scripts\activate
     ```

   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the development dependencies:

   ```
   pip install -r dev_requirements.txt
   ```

   This will install the `pre-commit` package and any other development-specific packages.

5. Set up the pre-commit hooks:

   ```
   pre-commit install
   ```

6. Run the test suite and ensure everything passes:

    ```
    python -m pytest tests/
    ```
