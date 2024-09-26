
import random
import math


#Exercice 6 / question 1
print("Exercice 6 / question 1:")
print("La formule permettant de calculer le volume du cylindre est: π(r**2)h")
print("La formule permettant de calculer la surface du cylindre est: 2πrh+2πr ")


#Exercice 6 / question 2
print("Exercice 6 / question 2:")
print("Les variables qu'on va utiliser sont: rayon(r) et hauteur(h). Ils sont tout deux de type float.")


#Exercice 6 / question 3
r = random.randint(1, 10)
h = random.randint(1, 10)
pi = (math.pi)

def volume_cylindre(r, h):
    volume = pi * (r**2) * h
    volumeApprox = round(volume, 2)
    return volumeApprox

def surface_cylindre(r, h):
    surface = (2 * pi * r * h) + (2 * pi * (r ** 2))
    surfaceApprox = round(surface, 2)
    return surfaceApprox

print("Exercice 6 / question 3:")
print("Le volume du cylindre avec rayon", r ,"et de hauteur", h , "est de", volume_cylindre(r, h))
print("La surface du cylindre avec rayon", r ,"et de hauteur", h , "est de", surface_cylindre(r, h))