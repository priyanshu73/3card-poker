import random
from card import Card
class Deck:
    def __init__(self):
        self.deck = [None]*52
    
    
    def generate(self):
        index = 0
        for i in range(2,15):
            for j in range(4):
                card = Card(i*10 + (j + 1))
                self.deck[index] = card
                index += 1
                
    def shuffle(self):
        for i in range(51, 0,-1):
            j = random.randint(0, i)
            self.deck[i] , self.deck[j] = self.deck[j], self.deck[i]
            

    def get_deck(self):
        return self.deck
    
    def show_deck(self):
        count = 0
        for i in self.deck: 
            print(str(i.getValue()) + " ", end = "")
      
    def draw_Card(self):
        if( len(self.deck) != 0):
            card = self.deck.pop()
            return card