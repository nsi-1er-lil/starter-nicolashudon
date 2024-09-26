import random
import math

#Exercice 5 / question 1
print("Exercice 5 / question 1:")
print("1. La formule pour calculer le perimetre d'une cercle est: 2πr ")


#Exercice 5 / question 2
print("Exercice 5 / question 2:")
print("2. L'argument est le rayon du cercle. Cet argument serait de type float")


#Exercice 5 / question 3
r = random.randint(1, 10)
pi = (math.pi)
def perimetre_cercle(r):
    perimetre = 2 * pi * r
    perimetreApprox = round(perimetre, 2)
    return perimetreApprox
print("Exercice 5 / question 3:")
print("Le perimetre du cercle de rayon", r , "est de environ ", perimetre_cercle(r))