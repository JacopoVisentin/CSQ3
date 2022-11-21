# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 18:02:20 2022

@author: Jacopo
"""

import random


# create a deck of cards
cards = []

# un loop qui cree les cartes tout seul pour pas devoir les faire moi meme
for suit in ["Spades", "Hearts", "Clubs", "Diamonds"]:
    for value in range(1, 14):
        cards.append((value, suit))


def simulation():
    toutesValeurs = [] #une liste pour stocker les 1000 valeurs pour chaque simulation pour pouvoir calculer la moyenne
    
    for i in range(1000):
        random.shuffle(cards)
        firstCard = cards[0] #regarde la premiere carte
        
        nombrePiochees = 0 #compteur pour voir la distance entre les deux cartes de meme valeur
        for carte in cards:
            if carte == cards[0]:
                pass #sert a ignorer la premiere carte pcq mtn on ne la pioche plus on la regarde juste donc elle reste dans le deck
            elif carte[0] == firstCard[0]: #si la valeur des deux cartes est la meme (elif veut dire else if)
                nombrePiochees += 1
                break #des qu'on trouve une carte avec la meme valeur on arrete la boucle
            else:
                nombrePiochees += 1
        toutesValeurs.append(nombrePiochees) # ajouter le resultat de cette simulation à la liste des resultats
    
    return sum(toutesValeurs)/len(toutesValeurs) #retourne la somme de tous les elements de la liste divisee par la longueur de la liste
                                                # càd la moyenne

print(simulation())