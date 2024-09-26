import random

#Exercice 4 / question 6

c = random.randint(1, 10)
P = c * 4
A = c ** 2
b = A > 5
print("Exercice 4 / question 6:")
print("On prend ", c, "comme la longueure d'un cote")
print("Le perimetre du carre est de", P)
print("L'aire du carre est de", A )
print("L'aire du carre est superieur a 5 ?", b)


#Exercice 4 / question 7
x = random.randint(1, 10)
def perimetre(x):
    return x * 4

print("Exercice 4 / question 7:")
print("Le perimetre du carre, calculer avec une fonction, en utilisant", x, "comme longueure d'un cote, est de", perimetre(x))

#Exercice 4 / question 8
def surface(x):
    return x ** 2

print("Exercice 4 / question 8:")
print("L'aire dur carre, calculer avec une fonction, en utilisant", x, "comme longueure d'un cote, est de", surface(x))

