"""
Auteur
Date
Titre : Inverseur de digits
Description : Inverse les chiffres d'un nombre
"""
def DigitInverter(Value):
      ModuloValue  = Value % 10
      Value = Value - ModuloValue
      Value = Value / 10
      return Value

OriginalValue = int(input("Invert this value : "))
NumberDigit = 0

Value = OriginalValue
while(Value >= 10):
      Value = DigitInverter(Value)
      NumberDigit = NumberDigit + 1
NumberDigit = NumberDigit + 1
print(NumberDigit)

Value = OriginalValue
Tab = [0] * NumberDigit
i = 0
while(i < NumberDigit):
      Digit = DigitInverter(OriginalValue)
      Tab[i] = Digit
      Value = Value / 10
      i = i + 1
      
i = 0
while(i < NumberDigit):
      print('%g' % Tab[i], sep = '', end = '')
      i  = i + 1
