"""
Deck is a standard deck of 52 playing cards
"""
import random
from Card import Card

class Deck:
    """ this represents a deck of cards """
    def __init__(self):
        self.cards = self._createDeck()
        self.discards = []

    def _createDeck(self):
        cards = []
        for suit in "Hearts Spades Diamonds Clubs".split():
            for value in "A 2 3 4 5 6 7 8 9 10 J Q K".split():
                cards.append(Card(suit,value))
        return cards

    def shuffle(self):
        """ shuffle the deck in place """
        random.shuffle(self.cards)

    def draw(self):
        """ remove top card from the deck and put in discards
            and return that top card
        """
        c = self.cards[0]
        self.cards = self.cards[1:]
        self.discards.append(c)
        return(c)

    def drawN(self,n):
        """ this returns a list of the first n cards in the deck
            and it moves them from d.cards to d.discards
        """
        c = self.cards[:n]
        self.cards = self.cards[n:]
        self.discards += c
        return(c)
