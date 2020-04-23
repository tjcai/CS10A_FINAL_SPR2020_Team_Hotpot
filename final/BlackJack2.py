"""
Blackjack is the classic card game where you try
to beat the dealer and both are trying to get as close
to 21 without going over.
"""
from Card import Card
from Deck import Deck

class BlackJackCard(Card):
    """
    A BlackJackCard is the same as a Card, except
    that the Ace is 11 points and the Face cards are 10
    """
    def val(self):
        """ this returns the numeric value of a card """
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

class BlackJackDeck(Deck):
    """
    A BlackJackDeck is a deck of BlackJackCards
    """
    def _createDeck(self):
        cards = []
        for suit in "Hearts Spades Diamonds Clubs".split():
            for value in "A 2 3 4 5 6 7 8 9 10 J Q K".split():
                cards.append(BlackJackCard(suit,value))
        return cards

class BlackJack:
    """
    This version of BlackJack uses inheritance to create
    a deck of BlackJackCards
    """
    def __init__(self):
        self.cards = BlackJackDeck()
    def play(self):
        dealer = self.cards.drawN(2)
        human = self.cards.drawN(2)
        print('dealer:',dealer[0],'hidden')
        print('player:',human[0],human[1])
        print('\n\n-------')
        print("You go first")
        human_hand = self.get_hit_human(human)
        print('\n\n-------')
        print("Now the Dealer's turn")
        dealer_hand = self.get_hit_dealer(dealer)
        print('\n\n-------')
        print("Game over:")
        if self.val(human)>self.val(dealer):
            print("You won!")
        else:
            print("The Dealer won")
        print('you')
        self.print_hand(human)
        print('dealer')
        self.print_hand(dealer)
        print("\n\n")


    def val(self,hand):
        v = sum([c.val() for c in hand])
        if v>21:
            return 0
        else:
            return v

    def print_hand(self,hand):
        print(self.val(hand),'points',end=": ")
        for c in hand:
            print(c,end=" ")
        print()

    def get_hit_human(self,player):
        more = True
        while more:
            handvalue = self.val(player)
            if handvalue>21:
                print("You lost")
                return player
            self.print_hand(player)
            hit = input("Hit? (y or n) ")
            more = (hit=='y')
            if more:
                player += self.cards.drawN(1)
                handvalue = self.val(player)
            else:
                print("player stays")
                self.print_hand(player)
        return player

    def get_hit_dealer(self,player):
        more = True
        self.print_hand(player)
        while more:
            handvalue = self.val(player)
            if handvalue>21:
                print("Dealer lost")
                return player
            more = (handvalue<17) and (handvalue>0)
            if more:
                print('Dealer is hit')
                player += self.cards.drawN(1)
                handvalue = self.val(player)
                more = (handvalue<17) and (handvalue>0)
                self.print_hand(player)
            else:
                print('Dealer stays')
                self.print_hand(player)
        return player

if __name__ == "__main__":
    print("Let's play BlackJack!")
    game = BlackJack()
    more = True
    while more:
        game.play()
        reply = input("continue? (y or n) ")
        more = (reply=='y')
    print("\n\n*** Next Round ***\n\n")
    print("Goodbye!")
