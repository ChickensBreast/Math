"""
Auteur
Date
Titre : Opération Division Entière
Description : Opération division entière représenté par le symbole // en python.
"""

Value1 = int(input("Value1 = "))
Value2 = int(input("Value2 = "))
def IntegerDivision(Value1, Value2):
    if(Value2 == 0):
        print("Error, the division by 0 isn't defined.")
        Value2 = int(input("Value2 = "))

    Count = 0
    if(Value1 > 0 and Value2 > 0):
        while(Value1 > Value2):
            Value1 = Value1 - Value2
            Count = Count + 1
        
    if(Value1 < 0 and Value2 > 0):
        while(-Value1 > Value2):
            Value1 = Value1 + Value2
            Count = Count + 1
        
    if(Value1 < 0 and Value2 > 0):
        while(Value1 > -Value2):
            Value1 = Value1 + Value2
            Count = Count + 1
        
    if(Value1 < 0 and Value2 < 0):
        while(-Value1 > -Value2):
            Value1 = Value1 - Value2
            Count = Count + 1

    print("La résultat de la division entière est : ", Count)
