import pytest

from war_game import Deck


def test_deck_initialization():
    deck = Deck()
    assert len(deck.cards) == 52, "Deck should have 52 cards"
    assert len(set(deck.cards)) == 13, "Deck should have 13 unique card values"

def test_deck_shuffling():
    deck1 = Deck()
    deck2 = Deck()
    assert deck1.cards != deck2.cards, "Two decks should be shuffled differently"

def test_deck_cutting():
    deck = Deck()
    half1, half2 = deck.cut_cards()
    assert len(half1) == len(half2) == 26, "Each half should have 26 cards"
