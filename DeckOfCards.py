# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 18:31:12 2022

@author: Jacopo
"""

import random

class Card:
    
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def getValue(self):
        return self.value
    
    def getSuit(self):
        return self.suit
        
    def __str__(self):
        return f"{self.getValue()} of {self.getSuit()}"




class Deck:
    
    def __init__(self):
        self.cards = []
        
        for suit in ["Spades", "Hearts", "Clubs", "Diamonds"]:
            for value in range(1, 14):
                self.cards.append(Card(value, suit))
    
    def shuffleDeck(self):
       random.shuffle(self.cards)
    
    def draw(self):
        self.lastDrawn = self.cards.pop(0)
        return self.lastDrawn
    
    def sameValueCard(self):
        for card in self.cards:
            if card.getValue() == self.lastDrawn.getValue():
                return card
   
    def position(self):
        return self.cards.index(self.sameValueCard()) + 1

    
    def __str__ (self):
        lst = []
        for card in self.cards:
            lst.append(card.__str__())
        return str(lst)
    
    
    
# myDeck = Deck()
# myDeck.shuffleDeck()
# print(myDeck)
# print(myDeck.draw())
# print(myDeck.sameValueCard())
# print(myDeck.position())

def simulatePosition():
    myDeck = Deck()
    myDeck.shuffleDeck()
    myDeck.draw()
    myDeck.sameValueCard()
    position = myDeck.position()
    
    return position
    
def simulateAverage():
    positions = []
    
    for i in range(1000):
        positions.append(simulatePosition())
    
    return sum(positions)/len(positions)

print(simulateAverage())