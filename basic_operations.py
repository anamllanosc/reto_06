class MathSymbolError(Exception):
    def __init__(self, message):
        super().__init__(message)

def basic_operations (x:int, y:int, z:str):

    if z == "+":
        return (x+y)
    elif z== "-":
        return (x-y)
    elif z== "*":
        return (x*y)
    elif z== "/":
        return (x/y)
    else: 
        raise MathSymbolError ("Simbolo matematico invalido")

try:     
    x=int(input("Ingrese el primer operando:"))
    y=int(input("Ingrese el segundo operando:"))
    z=str(input("¿Qué operación desea realizar?(+),(-),(*),(/):"))  

    print (basic_operations(x, y, z))

except ZeroDivisionError as e:
    print(f"Error: {e}")
except MathSymbolError as e:
    print(f"Error: {e}")