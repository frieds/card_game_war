"""
War Three Cards Game

This module contains the classes and logic for the War card game and three card variation. To play the game, create an
instance of the WarGame class and call the `play()` method. For more information and examples, see the README file.
"""

from random import shuffle
from collections import deque
from typing import List, Optional, Tuple
from enum import Enum


class CardValue(Enum):
    """Enumeration representing card values in a standard 52-card deck."""
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

    def __str__(self):
        return self.name.title()


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for card in CardValue:
                self.cards.append(card)
        shuffle(self.cards)

    def _half_deck_size(self) -> int:
        return int(len(self.cards)/2)

    def cut_cards(self) -> Tuple[List[CardValue], List[CardValue]]:
        """
        Returns: tuple containing two lists of CardValue, each representing half of the deck.
        """
        half_deck_size = self._half_deck_size()
        return self.cards[:half_deck_size], self.cards[half_deck_size:]


class Player:
    def __init__(self, name):
        self.stack = deque()
        self.name = name

    def draw_top_card(self):
        """Returns: top CardValue from the player's stack."""
        return self.stack.popleft()

    def draw_up_to_four_cards(self) -> List[CardValue]:
        """Returns: list of up to four CardValue from the player's stack."""
        up_to_four_cards = [self.stack.popleft() for _ in range(min(4, len(self.stack)))]
        return up_to_four_cards

    def add_cards(self, cards: [deque, List]):
        """
        Adds cards to the bottom of the player's stack.

        Args:
            cards: A deque or list of cards to be added to the player's stack.
        """
        shuffle(cards)
        self.stack.extend(cards)

    def has_cards(self):
        return bool(self.stack)


class WarGame:
    """
    A class to represent the War card game setup and play operations.

    Attributes
    ----------
    player1 : Player
        The first player in the game.
    player2 : Player
        The second player in the game.
    cards_pool : deque
        Holds the cards drawn from both players during a round.
    """

    def __init__(self, player1_name: str, player2_name: str):
        self.player1 = Player(name=player1_name)
        self.player2 = Player(name=player2_name)
        self.cards_pool = deque()

    def _cards_pool_str(self) -> str:
        return ', '.join(str(card) for card in self.cards_pool)

    def _deal_half_deck_to_each_player(self):
        deck = Deck()
        deck_half1, deck_half2 = deck.cut_cards()

        self.player1.add_cards(deck_half1)
        self.player2.add_cards(deck_half2)

    def _play_battle_round(self) -> Optional[Player]:
        """Returns: The Player instance who won the round or None if it was a tie."""
        player1_card = self.player1.draw_top_card()
        player2_card = self.player2.draw_top_card()
        print(f"{self.player1.name} draws {player1_card}")
        print(f"{self.player2.name} draws {player2_card}")

        self.cards_pool.extend([player1_card, player2_card])

        round_winner = self._determine_round_winner(player1_card, player2_card)
        return round_winner

    def _play_war_round(self) -> Optional[Player]:
        """Returns: The Player instance who won the round or None if it was a tie."""
        player1_cards = self.player1.draw_up_to_four_cards()
        player2_cards = self.player2.draw_up_to_four_cards()

        player1_card = player1_cards[-1]
        player2_card = player2_cards[-1]
        print(f"{self.player1.name} draws {player1_card}")
        print(f"{self.player2.name} draws {player2_card}")

        self.cards_pool.extend(player1_cards)
        self.cards_pool.extend(player2_cards)

        round_winner = self._determine_round_winner(player1_card, player2_card)
        return round_winner

    def _determine_round_winner(self, player1_card, player2_card) -> Optional[Player]:
        """Returns: The Player instance who won the round or None if it was a tie."""
        round_winner = None
        if player1_card.value < player2_card.value:
            round_winner = self.player2
        elif player1_card.value > player2_card.value:
            round_winner = self.player1
        return round_winner

    def play(self) -> Player:
        """
        Starts the game and continues until one of the players wins.
        Half the deck is dealt to each player, then runs battle rounds and war rounds as needed.
        Each round requires user input (pressing Enter) to proceed.

        Returns:
            The Player instance who won the game.
        """
        self._deal_half_deck_to_each_player()

        while self.player1.has_cards() and self.player2.has_cards():
            input("Press Enter to start the next round...")

            print("Battle!")
            round_winner = self._play_battle_round()
            if not round_winner:
                print("War!")
                while not round_winner and self.player1.has_cards() and self.player2.has_cards():
                    input("Press Enter to continue at war...")
                    round_winner = self._play_war_round()

            round_winner.add_cards(self.cards_pool)
            print(f"{round_winner.name} wins {len(self.cards_pool)} cards: {self._cards_pool_str()}")
            print(f"{self.player1.name} has {len(self.player1.stack)} cards")
            print(f"{self.player2.name} has {len(self.player2.stack)} cards\n")
            self.cards_pool.clear()

        if self.player1.has_cards():
            game_winner = self.player1
        else:
            game_winner = self.player2
        print(f"\n{game_winner.name} is the War game winner!")
        return game_winner
