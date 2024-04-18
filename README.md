# reto_06
## basic_operations.py
```python

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
```
Se capturan errores de tipo ZeroDivisionError, en caso de que la operación preferida sea la division y el numerador sea 0. Se crea la excepción de tipo MathSymbolError que captura como erroe el caso en que se ingrese un simbolo matematico diferente a +(suma), -(resta), *(multiplicación) o /(división). 
## prime_numbers.py
```python
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
    except ValueError as 
        print(f"Error: {e}")
    except ElementNumberError as e:
        print(f"Error: {e}")

```
Ocurre ValueError si se ingresa algo diferente a un digito, o si el digito ingresado no es un entero. Se crea la excepción ElementNumberError que captura como erroe el caso en que no se ingrese ningun elemento a la lista.
## maxsumconsecutivos.py
```python
class ElementNumberError(Exception):
    def __init__(self,message):
        super().__init__(message)
        
def max_sum (numbers_list):
    maxi_sum=0

    for i in range (len(numbers_list)-1):# rango de 0 a n-2 
        actual_sum=numbers_list[i]+numbers_list[i+1]# el ultimo i sera n-2 e i+1 sera n-1

        if actual_sum > maxi_sum:
            maxi_sum=actual_sum

    return maxi_sum

if __name__ == "__main__":  

    try:    
        n=int(input("Ingrese el numero de elementos que tendra la lista: "))
        if n<2:
            raise ElementNumberError ("La lista debe tener al menos dos elementos")

        numbers_list=[]
        for i in range (n):
            numbers_list.append(int(input("*"))) 

        print (f"La mayor suma de elementos consecutivos es: {max_sum(numbers_list)}")

    except ElementNumberError as e:
        print (f"Error: {e}")
    except ValueError:
        print(f"Error: El numero de elementos debe ser un digito entero")
```
Ocurre ValueError si se ingresa algo diferente a un digito, o si el digito ingresado no es un entero y ElementNumberError en caso de que la lista tega menos de dos elementos, debido a que es el mínimo que necesita para poder sumar comparar.
## same_charater.py
```python
class ElementNumberError(Exception):
    def __init__(self,message):
        super().__init__(message)

def same_characters(words_list):
    same_char_list=[]
    for i in range (len(words_list)):
        first_word=words_list[i]


        for j in range (i+1, len(words_list)):
            second_word=words_list[j]

            first_chars = sorted(list(first_word))
            second_chars = sorted(list(second_word))

            if first_chars == second_chars:
                same_char_list.append(first_word)
                same_char_list.append(second_word)
    return same_char_list


if __name__ == "__main__":
    try:
        words_list=[]
        n=int(input("Ingrese la cantidad de elementos de la lista:"))
        if n<=1:
            raise ElementNumberError ("Debe ingresar al menos dos elementos para comparar.")
        else:
            print(f"Ingrese las {n} palabras a comparar")
            for i in range (n):
                words_list.append(str(input("*")))

        for word in words_list:
            if word.isalpha()==False:
                raise ValueError("Los elementos de la lista solo pueden contener letras.")
            
        print(f"Los elementos con los mismos caracteres son: {same_characters(words_list)}")
                
            
    except ElementNumberError as e:
        print (f"Error: {e}")
    except ValueError as e:
        print (f"Error: {e}")
    
    
```
Se levanta la excepcion ValueError en caso de que se verifique que alguno de los elementos de la lista contiene al menos un digito o un signo y ElementNumberError en caso de que se ingresen menos de dos elementos, debido a que la idea es compararlos.
## palindromo.py
```python
class ElementNumberError(Exception):
    def __init__(self,message):
        super().__init__(message)

def palindrome (word):
    reversed_word=""

    if len(word)<=2:
        raise ElementNumberError ("La palabra ingresada debe tener al menos tres caracteres.")

    if word.isalpha():
        for letter in word:
            reversed_word = letter + reversed_word
            print(f"->{word} al reves= {reversed_word}")
    else:
        raise ValueError("Los elementos de la lista solo pueden contener letras.")

    if reversed_word.lower()==word.lower():
        return ("La palabra ingresada es un palindromo ")
    else:
        return ("La palabra ingresada no es un palindromo ")

try:
    word=str(input("¿Qué palabra desea que se verifique?"))
    print(palindrome(word))
except ElementNumberError as e:
    print (f"Error: {e}")
except ValueError as e:
    print (f"Error: {e}")
    
    
```
Si la palabra ingresada tiene menos de tres caracteres ocurre ElementNumberError, debido a que si se ingresa un solo caracter, siempre se consideraria un palíndromo, cuando no lo es. En caso de que algun elemento de la lista contenga al menos un digito o signo, ocurre ValueError
