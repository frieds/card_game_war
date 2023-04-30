import pytest

from war_game import CardValue, Player


@pytest.fixture
def player_with_cards():
    def _player_with_cards(name, cards):
        player = Player(name=name)
        player.stack.extend(cards)
        return player
    return _player_with_cards


@pytest.fixture
def player_with_set_cards():
    player = Player(name="Ready Player One")
    cards = [CardValue.ACE, CardValue.TWO, CardValue.FOUR]
    player.stack.extend(cards)
    return player


def test_draw_top_card(player_with_set_cards):
    drawn_card = player_with_set_cards.draw_top_card()
    assert drawn_card == CardValue.ACE
    assert list(player_with_set_cards.stack) == [CardValue.TWO, CardValue.FOUR]


@pytest.mark.parametrize("initial_cards, expected_drawn_cards, remaining_cards", [
    # have 5 cards, draw 4, 1 remaining
    ([CardValue.ACE, CardValue.TWO, CardValue.THREE, CardValue.FOUR, CardValue.FIVE],
     [CardValue.ACE, CardValue.TWO, CardValue.THREE, CardValue.FOUR],
     [CardValue.FIVE]),
    # have 4 cards, draw 4, 0 remaining
    ([CardValue.ACE, CardValue.TWO, CardValue.THREE, CardValue.FOUR],
     [CardValue.ACE, CardValue.TWO, CardValue.THREE, CardValue.FOUR],
     []),
    # have 3 cards, draw 3, 0 remaining
    ([CardValue.ACE, CardValue.TWO, CardValue.THREE],
     [CardValue.ACE, CardValue.TWO, CardValue.THREE],
     [])
])
def test_draw_up_to_four_cards(player_with_cards, initial_cards, expected_drawn_cards, remaining_cards):
    player = player_with_cards("Test Player", initial_cards)
    drawn_cards = player.draw_up_to_four_cards()

    assert drawn_cards == expected_drawn_cards
    assert list(player.stack) == remaining_cards


def test_add_cards(player_with_set_cards):
    new_cards = [CardValue.SIX, CardValue.SEVEN]
    player_with_set_cards.add_cards(new_cards)

    # Since the cards are shuffled, we can't compare the order directly.
    # Instead, we can check that the lengths match and that the cards are in the player's stack.
    assert len(player_with_set_cards.stack) == 5
    for card in new_cards:
        assert card in player_with_set_cards.stack


def test_has_cards(player_with_set_cards):
    assert player_with_set_cards.has_cards()

    # Remove all cards from the player's stack
    for _ in range(len(player_with_set_cards.stack)):
        player_with_set_cards.stack.pop()

    assert not player_with_set_cards.has_cards()
