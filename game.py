from deck import Deck, Card

class Hand:
    """
    A class representing a 5-card poker hand dealt from a Deck.
    Provides methods to evaluate the type of hand (e.g., flush, pair, straight).
    """

    def __init__(self, deck):
        """
        Deal 5 cards from the provided Deck and store them in the hand.

        :param deck: Deck instance from which to deal the hand.
        """
        cards = []
        for i in range(5):
            cards.append(deck.deal())
        self._cards = cards

    @property
    def cards(self):
        """
        Get the list of cards in the hand.

        :return: list of Card objects.
        """
        return self._cards

    def __str__(self):
        """
        String representation of the hand.

        :return: str representation of the list of cards.
        """
        return str(self.cards)

    @property
    def is_flush(self):
        """
        Check if all cards in the hand have the same suit.

        :return: True if the hand is a flush, False otherwise.
        """
        for card in self.cards[1:]:
            if self.cards[0].suit != card.suit:
                return False
        return True

    @property
    def num_matches(self):
        """
        Count the number of matching ranks among all cards.

        :return: An integer representing the number of rank matches.
        """
        matches = 0
        for i in range(5):
            for j in range(5):
                if i == j:
                    continue
                if self.cards[i].rank == self.cards[j].rank:
                    matches += 1
        return matches

    @property
    def is_pair(self):
        """
        Check if the hand contains exactly one pair.

        :return: True if it's a pair, False otherwise.
        """
        if self.num_matches == 2:
            return True
        return False

    @property
    def is_2_pair(self):
        """
        Check if the hand contains exactly two pairs.

        :return: True if it's two pair, False otherwise.
        """
        if self.num_matches == 4:
            return True
        return False

    @property
    def is_trips(self):
        """
        Check if the hand contains three of a kind.

        :return: True if it's trips (three of a kind), False otherwise.
        """
        if self.num_matches == 6:
            return True
        return False

    @property
    def is_quads(self):
        """
        Check if the hand contains four of a kind.

        :return: True if it's quads (four of a kind), False otherwise.
        """
        if self.num_matches == 12:
            return True
        return False

    @property
    def is_full_house(self):
        """
        Check if the hand is a full house (three of a kind and a pair).

        :return: True if it's a full house, False otherwise.
        """
        if self.num_matches == 8:
            return True
        else:
            return False

    @property
    def is_straight(self):
        """
        Check if the hand is a straight (five cards in sequence, no repeats).

        :return: True if the hand is a straight, False otherwise.
        """
        if self.num_matches != 0:
            return False
        self.cards.sort()
        if Card.RANKS.index(self.cards[-1].rank) != \
                Card.RANKS.index(self.cards[0].rank) + 4:
            return False
        return True


# Simulate drawing hands and estimate the probability of getting a straight
matches = 0
count = 0
while matches < 1000:
    deck = Deck()
    deck.shuffle()
    hand = Hand(deck)
    count += 1
    if hand.is_straight:
        # print(hand)
        matches += 1
        # break

print(f"The probability of straight is {100*matches/count}%")