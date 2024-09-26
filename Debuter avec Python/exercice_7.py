#Exercice 7 / question 1
print("Exercice 7 / question 1:")
print("Les variables de la fonction dont la taille et la masse. Ces variables sont tous deux des floats.")


#Exercice 7 / question 2
print("Exercice 7 / question 2:")
print("La fonction doit renvoyer l'IMC de l'individu. Cette valeur sera de type float")


#Exercice 7 / question 3
import random

def IMC(m, t):
    imc = m / (t ** 2)
    imcApprox = round(imc, 2)
    return imcApprox


#Exercice 7 / question 4
m = 65
t = 1.75
print("Exercice 7 / question 4:")
print("L'IMC d'une personne avec une masse de", m , "kg et une taille de", t , "m est de", IMC(m,t) )
