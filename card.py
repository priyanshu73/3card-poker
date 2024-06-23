class Card:
    def __init__(self, value):
        self.suit = value%10 
        self.rank = int(value/10)
        
    def getValue(self):
        return self.rank * 10 + self.suit


    def set_suit(self, new_suit):
        if new_suit in [1, 2, 3,4]:
            self.suit = new_suit
        else:
            raise ValueError("Invalid suit. Valid suits are Hearts, Diamonds, Spades, and Clubs.")
  
    def set_rank(self, new_rank):
        if new_rank >= 1 and new_rank <=13:
            self.rank = new_rank
        else:
            raise ValueError("Invalid rank")

    def get_name(self):
        suits = {
        1: 'Clubs',
        2: 'Diamonds',
        3: 'Hearts',
        4: 'Spades'
    }
        
        ranks = {
            11 : 'Jack',
            12 : 'Queen',
            13 : 'King',
            14 : 'Ace'
        }
        type = suits.get(self.suit, 'Invalid')
        value = 0
        if (self.rank in [11,12,13,14]):
            value = ranks.get(self.rank, 'Invalid')
        else:
            value = self.rank
        
        return str(value) + " of " + str(type) 
    
