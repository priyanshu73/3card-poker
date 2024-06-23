from hand import Hand
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        
    def give_Card(self, card):
        self.hand.add_Card(card)
    
    def winner(self, player1):
        if self.hand.give_HigherHand(player1.hand) == self.hand:
            return self
        else:
            return player1
    