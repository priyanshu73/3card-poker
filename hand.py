from deck import Deck
from card import Card
import os
import random
class Hand:
    def __init__(self):
        
        self.cards = []
    
    
    def clear(self):
        self.cards = []
        
    def add_Card(self,card):
        self.cards.append(card)
    
    def identify_hand(self):
        if(self.is_trial()):
            return "trial"
        elif(self.is_doubleRun()):
            return "double_run"
        elif(self.is_Run()):
            return "run"
        elif(self.is_Color()):
            return "color"  
        elif(self.is_double()):
            return "double"
        else:
            return "high_card"
    
    def is_double(self):
        x = self.cards[0].rank
        y = self.cards[1].rank
        z = self.cards[2].rank
        hand_cards = [x,y,z]
        hand_cards.sort()
        x = hand_cards[0]
        y = hand_cards[1]
        z = hand_cards[2]

    
        if((x == y != z) or (y == z != x)):
            return True
        return False
    
    def is_Color(self):
        if self.cards[0].suit == self.cards[1].suit == self.cards[2].suit:
            return True
        return False
    
    def is_Run(self):
        x = self.cards[0].rank
        y = self.cards[1].rank
        z = self.cards[2].rank
        
        hand_cards = [x,y,z]
        hand_cards.sort()
        x = hand_cards[0]
        y = hand_cards[1]
        z = hand_cards[2]

        
  
        if (z == y + 1 and y == x + 1) or ( x == 2 and y == 3 and z == 14):
            return True 
        
        return False
    
    def is_doubleRun(self):
        if(self.is_Run() and self.is_Color()):
            return True
        return False
    
    def is_trial(self):
        if (self.cards[0].rank == self.cards[1].rank == self.cards[2].rank):
            return True
        return False
        
    
    def show_hand(self):
        print(str(self.cards[0].getValue()) + " " + str(self.cards[1].getValue()) + " " + str(self.cards[2].getValue()))

    def get_hand(self):
        list = [self.cards[0].getValue(), self.cards[1].getValue(), self.cards[2].getValue()]
        return list
    
    def get_handRanks(self):
        list = [int(x/10) for x in self.get_hand()]
        return list
    
    def compare_hands(self, hand_x):
        if (self.identify_hand() == hand_x.identify_hand()):
            
            hand1 = self.get_handRanks()
        
            hand2 = hand_x.get_handRanks()
            
            hand1.sort()
     
            hand2.sort()
            
            x1 = hand1[0]
            y1 = hand1[1]
            z1 = hand1[2]
 
            x2 = hand2[0]
            y2 = hand2[1]
            z2 = hand2[2]

        self.show_hand()
        hand_x.show_hand()

        for i in range(3):
             if( z1 > z2):
                 return self
             elif( z2 > z1):
                 return hand_x
             elif( y1 > y2):
                 return self
             elif( y2 > y1):
                 return hand_x
             elif( x1 > x2):
                 return self
             elif(x2 > x1) :
                 return hand_x
             else:
                 return -1
      
    
    def hand_Value(self):
         if(self.is_trial()):
            return 30
         elif(self.is_doubleRun()):
            return 25
         elif(self.is_Run()):
            return 20
         elif(self.is_Color()):
            return 15  
         elif(self.is_double()):
            return 10
         else:
            return 5
        
    def give_HigherHand(self, hand_x):
        if(self.hand_Value() > hand_x.hand_Value()):
            return self
        elif(self.hand_Value() < hand_x.hand_Value()) :
            return hand_x
        else:
            return self.compare_hands(hand_x)
    
    
        
os.system('cls')
deck = Deck()
deck.generate()
deck.show_deck()

print()
print()
hand2 = Hand()
hand2.add_Card(Card(33))
hand2.add_Card(Card(132))
hand2.add_Card(Card(83))

hand3 = Hand()
hand3.add_Card(Card(144))
hand3.add_Card(Card(91))
hand3.add_Card(Card(44))

hand2.show_hand()
hand3.show_hand()

print(hand2.identify_hand() + " " + hand3.identify_hand())


hand_f = hand2.give_HigherHand(hand3)

if isinstance(hand_f,int):
    cards = "draw, no one"
    type = ""
else:
    cards = hand_f.get_hand()
    type = hand_f.identify_hand()

    


print(str(cards) + type + " wins")

decK = deck.get_deck()


print()

'''
handType = []
handList = []

cc = 0
rc = 0
hcc = 0
drc = 0
tc = 0
dc = 0
condt = True
c = 0
a = 0
b = 0
d = 0

while(not condt):
    hand2 = Hand()
    decK = deck.get_deck()
    
    a = 51
    b = 49
    d = 47
    hand2.add_Card(decK[a])
    hand2.add_Card(decK[b])
    hand2.add_Card(decK[d])
    
    handType.append(str(hand2.identify_hand()))  
    result = str(hand2.identify_hand())
    
    if(result== "high_card"):
        hcc += 1
    elif(result== "double"):
        dc += 1
    elif(result== "color"):
        cc += 1
    elif(result== "run"):
        rc += 1
    elif(result== "double_run"):
        drc += 1
    else:
        tc +=1
        
    handList.append(str(hand2.get_hand()))
    deck.shuffle()
    c += 1
    if(c == 10000): 
        condt = False
    
#print(handType)

#print(handList)


data = {}
for key in handList:
    for value in handType:
        data[key] = value
        handType.remove(value)
        break
#os.system('cls')
print(str(data))




print( "Hands Played  until: " + str(c) )

print( " high_card count: " + str(round(hcc/c * 100, ndigits=1)) )
print( " double count: " + str(round(dc/c *100, ndigits=1)) )
print( " color count: " + str(round(cc/c*100, ndigits=1)) )

print( " run count: " + str(round(rc/c*100, ndigits=1))  )
print( " double_run: " + str(round(drc/c*100, ndigits=1))  )
print( " trial: " + str(round(tc/c*100, ndigits=1))  )

''' 