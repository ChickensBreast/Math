"""
Auteur
Date
Titre : Opération Modulo
Description : Opération de modulo
"""


Nb1 = int(input("Nb1 = "))
Nb2 = int(input("Nb2 = "))

Compteur = 0
if(Nb1 > 0 and Nb1 > Nb2):
    Nb1 = Nb1 - Nb2
    Resultat = Nb1
elif(Nb1 < 0 and Nb1 < Nb2):
    Nb1 = Nb1 + Nb2
    Resultat = Nb1
else:
    Resultat = 0

print("Le resultat du modulo : ", Resultat)
