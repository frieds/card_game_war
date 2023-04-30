from collections import deque

import pytest

from war_game import CardValue, WarGame


@pytest.fixture
def custom_wargame():
    game = WarGame("Player1", "Player2")
    # do not change these card values. They're needed as is for tests
    game.player1.stack = deque([CardValue.TWO, CardValue.FOUR, CardValue.SIX, CardValue.EIGHT])
    game.player2.stack = deque([CardValue.THREE, CardValue.FIVE, CardValue.SEVEN, CardValue.NINE])
    return game


def test_deal_half_deck_to_each_player():
    # Given
    game = WarGame("Player1", "Player2")

    # When
    game._deal_half_deck_to_each_player()

    # Then
    assert len(game.player1.stack) == 26
    assert len(game.player2.stack) == 26
    assert set(game.player1.stack).union(set(game.player2.stack)) == set(CardValue)


def test_play_battle_round(custom_wargame):
    # Given
    player1_card_top_card = custom_wargame.player1.stack[0]
    player2_card_top_card = custom_wargame.player2.stack[0]

    # When
    round_winner = custom_wargame._play_battle_round()

    # Then
    assert len(custom_wargame.cards_pool) == 2
    assert player1_card_top_card in custom_wargame.cards_pool
    assert player2_card_top_card in custom_wargame.cards_pool
    assert round_winner == custom_wargame.player2


def test_play_war_round(custom_wargame):
    # Given / When
    round_winner = custom_wargame._play_war_round()

    # Then
    assert len(custom_wargame.cards_pool) == 8

    for card in list(custom_wargame.player1.stack)[:4]:
        assert card in custom_wargame.cards_pool

    for card in list(custom_wargame.player2.stack)[:4]:
        assert card in custom_wargame.cards_pool

    assert round_winner == custom_wargame.player2


class CustomWarGame(WarGame):
    def _deal_half_deck_to_each_player(self):
        pass


def test_game_end_when_player_has_no_cards(custom_wargame):
    # Given
    custom_wargame = CustomWarGame("Test Player1", "Test Player2")

    # Empty player1's stack and give player2 3 cards
    custom_wargame.player1.stack.clear()
    custom_wargame.player2.stack.extend([CardValue.TWO, CardValue.FOUR, CardValue.SIX])

    # When
    game_winner = custom_wargame.play(input_function=lambda _: "")

    # Then
    assert game_winner == custom_wargame.player2
    assert len(custom_wargame.player1.stack) == 0
    assert len(custom_wargame.player2.stack) == 3
