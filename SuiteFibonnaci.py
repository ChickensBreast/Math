"""
Auteur
Date
Titre : Suite de Fibonnacci
Description :
===========================================
1, 1,  2, 3, 5, 8, 13, 21, 34 ...
0+1 , 1+1, 1+2, 3+5, 8+5 + 13+8, 21 + 13
===========================================
Problème du lapin de Fibonnacci

Nombre d'or = (1+sqrt(5)) / 2 ~ 1.6180339887 ...
Reponse positive de x² - x - 1 = 0



Source : Pour La Science Numero 478
"""

NombreElement = int(input("Entrer le nombre d'élément à afficher de la suite de Fibonnacci : "))
NombreElementTraite = 0

Nombre1 = 0
Nombre2 = 1

print(Nombre2)
while(NombreElementTraite < NombreElement - 1):
            NombreSuite = Nombre1 + Nombre2
            print(NombreSuite, sep = " ,")
            Nombre1 = Nombre2
            Nombre2 = NombreSuite
            NombreElementTraite = NombreElementTraite + 1
