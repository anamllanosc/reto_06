class ElementNumberError(Exception):
    def __init__(self,message):
        super().__init__(message) 

def prime_number(numbers_list):
    primes_list=[]
    for number in numbers_list:
        divisors=[]
        for i in range (1,number):
            if number%i==0:
                divisors.append(i)
        if len(divisors)==1:
            primes_list.append(number)
    return primes_list
    
if __name__ == "__main__":

    try:
        numbers_list=[]
        n=int(input("Ingrese la cantidad de elementos de la lista:"))
        if n<1:
            raise ElementNumberError("Usted no ingreso ningun elemento a la lista")
        for i in range (n):
            numbers_list.append(int(input("*")))
        if len(prime_number(numbers_list)) < 1:
             print(f"Ninguno de los numeros que ingresó es un número primo")
        else:
            print(f"Los numeros primos de la lista que acaba de ingresar son: {prime_number(numbers_list)}")
    except ValueError as e:#Ocurre "ValueError" si se ingresa algo diferente a un digito, o si el digito ingresado no es un entero.
        print(f"Error: {e}")
    except ElementNumberError as e:
        print(f"Error: {e}")

    