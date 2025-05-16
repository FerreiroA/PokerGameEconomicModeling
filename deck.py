import random

class Card:
    """
    A class representing a playing card with a rank and a suit.
    """

    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["♣", "♦", "♥", "♠"]
    # SUITS = ["clubs", "diamonds", "hearts", "spades"]

    def __init__(self, rank, suit):
        """
        Initialize a Card with a specified rank and suit.

        :param rank: The rank of the card (must be in RANKS).
        :param suit: The suit of the card (must be in SUITS).
        :raises ValueError: if rank or suit are invalid.
        """
        if rank not in self.RANKS:
            raise ValueError("invalid rank")
        if suit not in self.SUITS:
            raise ValueError("invalid suit")
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        """
        Get the rank of the card.

        :return: str
        """
        return self._rank

    @property
    def suit(self):
        """
        Get the suit of the card.

        :return: str
        """
        return self._suit

    def __str__(self):
        """
        Return the string representation of the card.

        :return: str in the format "<rank><suit>"
        """
        return f"{self._rank}{self._suit}"

    def __repr__(self):
        """
        Return the official string representation of the card.

        :return: str, same as __str__
        """
        return self.__str__()

    def __eq__(self, other):
        """
        Compare two cards for equality based on rank.

        :param other: Another Card object.
        :return: True if ranks are equal, False otherwise.
        """
        return self.rank == other.rank

    def __lt__(self, other):
        """
        Compare two cards by rank order.

        :param other: Another Card object.
        :return: True if this card is ranked lower than the other.
        """
        return self.RANKS.index(self.rank) < self.RANKS.index(other.rank)


class Deck:
    """
    A class representing a standard deck of 52 playing cards.
    """

    def __init__(self):
        """
        Initialize a full deck of 52 unique playing cards.
        """
        _cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                _cards.append(Card(rank, suit))
        self._cards = _cards

    @property
    def cards(self):
        """
        Get the list of cards currently in the deck.

        :return: List of Card objects.
        """
        return self._cards

    def __str__(self):
        """
        Return the string representation of the deck.

        :return: str
        """
        return str(self._cards)

    def shuffle(self):
        """
        Shuffle the deck in place using random.shuffle().
        """
        random.shuffle(self.cards)

    def deal(self):
        """
        Deal (remove and return) the top card from the deck.

        :return: Card object
        """
        return self.cards.pop(0)


if __name__ == "__main__":
    """
    Main block to test the Card and Deck classes.
    - Creates a card and prints its properties.
    - Creates, shuffles, and deals from a deck.
    """
    c1 = Card("A", "♣")
    print(c1.suit, c1.rank)
    deck = Deck()
    print(deck)
    deck.shuffle()
    print(deck)
    print(deck.deal())
    print(deck)