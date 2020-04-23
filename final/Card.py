class Card:
    """ Card represents a standard playing card """

    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return str(self.value) + " of " + str(self.suit)

    def __repr__(self):
        return 'Card("'  +  self.suit +  '","'  +  self.value +  '")'

    def __eq__(self,other):
        """Overrides the default implementation"""
        if isinstance(other, Card):
            return self.suit == other.suit and self.value==other.value
        return False

    def val(self,game='usual'):
        """ this returns the numeric value of a card """
        if game=='usual':
            if self.value in "2 3 4 5 6 7 8 9 10".split():
                return int(self.value)
            elif self.value == "J":
                return 11
            elif self.value == "Q":
                return 12
            elif self.value == "K":
                return 13
            elif self.value == "A":
                return 14
        elif game=='blackjack':
            if self.value in "2 3 4 5 6 7 8 9 10".split():
                return int(self.value)
            elif self.value == "J":
                return 10
            elif self.value == "Q":
                return 10
            elif self.value == "K":
                return 10
            elif self.value == "A":
                return 11

        
