blacktype  class:
  card: rank&suit(image)
  hand:collection of cards
      hit(+1),score(sum)
  deck:collection of cards
      shuffle,deal
      
      
# Testing template for the Hand class
http://www.codeskulptor.org/#user40_fLmdH3fAUz_0.py

import random

# define globals for cards
SUITS = ['C', 'S', 'H', 'D']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (card_size[0] * (0.5 + RANKS.index(self.rank)), card_size[1] * (0.5 + SUITS.index(self.suit)))
        canvas.draw_image(card_images, card_loc, card_size, [pos[0] + card_size[0] / 2, pos[1] + card_size[1] / 2], card_size)


#####################################################
# Student should insert code for Hand class here
class Hand:
    def __init__(self):
        #cards on hand:
        self.cards = []

    def __str__(self):
        Hand_contains = 'Hand contains'
        for handcard in self.cards:
            Hand_contains += ' ' + str(handcard) + ' '
        return Hand_contains
    
    def add_card(self,card):
        return self.cards.append(card)
         
    
###################################################
# Test code

c1 = Card("S", "A")
c2 = Card("C", "2")
c3 = Card("D", "T")
print c1, c2, c3
print type(c1), type(c2), type(c3)

test_hand = Hand()
print test_hand

test_hand.add_card(c1)
print test_hand

test_hand.add_card(c2)
print test_hand

test_hand.add_card(c3)
print test_hand

print type(test_hand)


###################################################
# Output to console
# note that the string representation of a hand will 
# vary based on how you implemented the __str__ method

#SA C2 DT
#<class '__main__.Card'> <class '__main__.Card'> <class '__main__.Card'>
#Hand contains 
#Hand contains SA 
#Hand contains SA C2 
#Hand contains SA C2 DT 
#<class '__main__.Hand'>


# Testing template for the Deck class


import random

# define globals for cards
SUITS = ['C', 'S', 'H', 'D']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}











http://www.codeskulptor.org/#user40_TEhwYhkvcv_0.py
# Testing template for the Hand class

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (card_size[0] * (0.5 + RANKS.index(self.rank)), card_size[1] * (0.5 + SUITS.index(self.suit)))
        canvas.draw_image(card_images, card_loc, card_size, [pos[0] + card_size[0] / 2, pos[1] + card_size[1] / 2], card_size)


#####################################################
# Student should insert code for Deck class here
class Deck:
    def __init__(self):     
        #self.suit = suit
        #self.card = card
        self.crads = []
        for suit in SUITS:
            for rank in RANKS:
                cards = Card(suit,rank)
                self.crads.append(cards)
     
    def __str__(self):    
        Deck_contains = 'Deck_contains'
        for deckcard in self.crads :
            Deck_contains += ' ' + str(deckcard) + ' '
        return Deck_contains
    
    def deal_card(self):
        deal_card = self.crads.pop()
        return deal_card
        
    def shuffle(self):
        random.shuffle(self.crads)
    
###################################################
# Test code

test_deck = Deck()
print test_deck
print type(test_deck)

c1 = test_deck.deal_card()
print c1
print type(c1)
print test_deck
print ''

c2 = test_deck.deal_card()
print c2
print type(c2)
print test_deck
print ''

test_deck = Deck()
print test_deck
print ''

test_deck.shuffle()
print test_deck
print type(test_deck)
print ''

c3 = test_deck.deal_card()
print c3
print type(c3)
print test_deck




###################################################
# Output to console
# output of string method for decks depends on your implementation of __str__
# note the output of shuffling is randomized so the exact order of cards
# need not match

#Deck contains CA C2 C3 C4 C5 C6 C7 C8 C9 CT CJ CQ CK SA S2 S3 S4 S5 S6 S7 S8 S9 ST SJ SQ SK HA H2 H3 H4 H5 H6 H7 H8 H9 HT HJ HQ HK DA D2 D3 D4 D5 D6 D7 D8 D9 DT DJ DQ DK 
#<class '__main__.Deck'>
#DK
#<class '__main__.Card'>
#Deck contains CA C2 C3 C4 C5 C6 C7 C8 C9 CT CJ CQ CK SA S2 S3 S4 S5 S6 S7 S8 S9 ST SJ SQ SK HA H2 H3 H4 H5 H6 H7 H8 H9 HT HJ HQ HK DA D2 D3 D4 D5 D6 D7 D8 D9 DT DJ DQ 
#DQ
#<class '__main__.Card'>
#Deck contains CA C2 C3 C4 C5 C6 C7 C8 C9 CT CJ CQ CK SA S2 S3 S4 S5 S6 S7 S8 S9 ST SJ SQ SK HA H2 H3 H4 H5 H6 H7 H8 H9 HT HJ HQ HK DA D2 D3 D4 D5 D6 D7 D8 D9 DT DJ 
#Deck contains CA C2 C3 C4 C5 C6 C7 C8 C9 CT CJ CQ CK SA S2 S3 S4 S5 S6 S7 S8 S9 ST SJ SQ SK HA H2 H3 H4 H5 H6 H7 H8 H9 HT HJ HQ HK DA D2 D3 D4 D5 D6 D7 D8 D9 DT DJ DQ DK 
#Deck contains CT H6 C4 H9 D6 HJ D2 S5 D8 H2 ST H4 HQ HK S8 D3 CJ D5 DK DQ DA S9 S6 S2 DJ C8 SJ C9 D4 C7 SK CK S3 CA SA S4 CQ S7 HA H3 C5 D9 DT H7 HT C2 SQ H8 C6 D7 C3 H5 
#<class '__main__.Deck'>
#H5
#<class '__main__.Card'>
#Deck contains CT H6 C4 H9 D6 HJ D2 S5 D8 H2 ST H4 HQ HK S8 D3 CJ D5 DK DQ DA S9 S6 S2 DJ C8 SJ C9 D4 C7 SK CK S3 CA SA S4 CQ S7 HA H3 C5 D9 DT H7 HT C2 SQ H8 C6 D7 C3 

