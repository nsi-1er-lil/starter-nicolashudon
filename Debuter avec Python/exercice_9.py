import random
def aMoyenne(vI, vF, t):

   #Exercice 9
    a = (vF - vI) / t
    aApprox = round(a, 2)
    return aApprox
vI = random.randint(1, 50)
vF = random.randint(1, 50)
t = random.randint(5, 30)

print("Exercice 9:")
print("L'acceleration moyenne avec une vitesse initiale de", vI, "m/s et une vitesse finale de", vF, "m/s sur une duree de", t, "secondes est de", aMoyenne(vI, vF, t), "m/s²")