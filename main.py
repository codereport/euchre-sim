#!/usr/bin/env python3

from itertools import product
from random import shuffle

from more_itertools import chunked

cards_t = list[tuple[int, int]]

def make_deck() -> cards_t:
    return list(product(range(9, 14), range(0, 4)))

def num_to_suit(num: int) -> str:
    assert 0 <= num and num <= 3
    return "♥♦♠♣"[num]

def num_to_face_value(num: int) -> str:
    assert 9 <= num and num <= 14
    return "8TJQKA"[num - 9]

def cards_to_string(cards: cards_t) -> str:
    return " ".join(f"{num_to_face_value(val)}{num_to_suit(suit)}" for val, suit in cards)

def deal(deck: cards_t) -> list[cards_t]:
    return list(chunked(deck, 5))[0:4]

def play_game():
    deck = make_deck()
    print("Deck:")
    print(cards_to_string(deck))
    shuffle(deck)
    print("Shuffle:")
    print(cards_to_string(deck)) # shuffle
    print("Deal:")
    players = deal(deck)
    for i, player in enumerate(players, 1):
        print(f"P{i}: {cards_to_string(player)}")

play_game()
