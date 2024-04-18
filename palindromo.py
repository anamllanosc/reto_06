class ElementNumberError(Exception):
    def __init__(self,message):
        super().__init__(message)

def palindrome (word):
    reversed_word=""

    if len(word)<=2:
        raise ElementNumberError ("La palabra ingresada debe tener al menos dos caracteres.")

    digit = False
    for letter in word:
        if letter.isdigit():
            digit = True
            break  # Si ya encontramos un dígito, podemos salir del bucle
        else:
            reversed_word = letter + reversed_word
            print(f"->{word} al reves= {reversed_word}")

    if digit:
        raise ValueError("Los elementos de la lista no pueden contener digitos.")

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
    