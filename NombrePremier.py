"""
Auteur
Date
Titre : Value Prime Serie
Description :
"""

Value = 2
ElementOutput = 0
ElementInput = int(input("Value de chiffres premiers : "))

while(ElementOutput < ElementInput):
    IsPrime = True
    Divisor = Value - 1
    while(Divisor > 1 and IsPrime == True):
        if(Value % Divisor == 0):
            IsPrime = False
        else:
            IsPrime = True
            Divisor = Divisor - 1
    if(IsPrime == True):
        ElementOutput = ElementOutput + 1 
        print(Value)
             
    Value = Value + 1
    
