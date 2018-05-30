"""
Auteur
Date
Titre : Palindrome nombre
Description : Verification des nombre palindromes
"""

Nombre = int(input("Nombre à inverser : "))
NombreDigit = 0
while(Nombre >= 10):
      NombreModulo  = Nombre % 10
      Nombre = Nombre - NombreModulo
      Nombre = Nombre / 10
      NombreDigit = NombreDigit + 1
NombreDigit = NombreDigit + 1
print(NombreDigit)

EstPremier = True
Diviseur = Nombre - 1
while(Diviseur > 1 and EstPremier == True):
      if(Nombre % Diviseur == 0):
            EstPremier = False
      else:
            EstPremier = True
            Diviseur = Diviseur - 1
      
Tab = [0] * NombreDigit
i = 0
while(i < NombreDigit):
      Digit = Nombre % 10
      Tab[i] = Digit
      Nombre = Nombre - Digit
      Nombre = Nombre / 10
      i = i + 1
      
i = 0
while(i < NombreDigit):
      if(Tab[i] == Tab[NombreDigit - i]):
            print("La valeur", Nombre, "est un palindrome.")
      elif:(Tab[i] == Tab[NombreDigit - i]):
            print("La valeur", Nombre, "est un palindrome premier.")
      i  = i + 1
