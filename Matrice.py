"""
Auteur
Date
Titre : Opérateur de base sur matrice
Description : Addition de deux matrices, Multiplication matricielle
"""
import numpy

def VerificationCompatibiliteTailleAddition(varI, varJ, varK, varL):
      if(varI == varK and varJ == varL):
                  MatriceTailleIdentique = True

def DefinitionDimensionDesMatrices(varI, varJ, varK, varL):
      if(varJ == varK):
            MatriceTailleCompatibleMultiplication = True

print("1- Addition / Soustraction entre deux matrices")
print("2- Multiplication de deux matrices")

Option = input("Choisir votre option : ")

if(Option == 1):
      MatriceTailleIdentique = False
      while(MatriceTailleIdentique == False):
            varI, varJ = input("Entrer la taille de la matrice A de dimension i par j : ").split(" ")
            varK, varL = input("Entrer la taille de la matrice B de dimension k par l : ").split(" ")
            VerificationCompatibiliteTailleAddition

elif(Option == 2):
      MatriceTailleCompatibleMultiplication = False
      while(MatriceTailleCompatibleMultiplication = False):
            varI, varJ = input("Entrer la taille de la matrice A de dimesion i par j : ").split(" ")
            varK, varL = input("Entrer la taille de la matrice B de dimension k par l : ").split(" ")
            if(varJ == varK):
                  MatriceTailleCompatibleMultiplication = True

            MatriceA = numpy.zeros((i, k))
            MatriceB = numpy.zeros((k, l))
            MatriceC = numpy.zeros((i, l ))
            
            i = 0
            j = 0
            k = 0
            l = 0

            for
            MatriceC = MatriceA[i][j] * Matrice[k][l] 
