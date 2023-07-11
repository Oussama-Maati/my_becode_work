# Exo 1
import random


def int_to_str(num: int) -> str:
    return str(num)


# Exo 2
def int_div(num: int, div: int) -> float:
    return num / div


# Exo 3
def send_email(address: str,
               sender: str,
               cc: str,
               cci: str,
               subject: str = '',
               body: str = None) -> str:
    return "mail"


# Exo 4
from typing import Tuple, List, Mapping

suits = "♠ ♡ ♢ ♣".split()
ranks = "2 3 4 5 6 7 8 9 10 J Q K A".split()

Card = Tuple[str, str]
Deck = List[Card]
Players = [str, [Card]]


def shuffle_distri() -> None:
    Players = [["Alice", []], ["Bob", []], ["Nathan", []], ["Maria", []]]
    Deck = [(suit, rank) for suit in suits for rank in ranks]
    print(Deck)

    while Deck:
        for Player in Players:
            randomCard = random.choice(Deck)
            Player[1].append(randomCard)
            Deck.remove(randomCard)

    for player in Players:
        print(player)


shuffle_distri()
