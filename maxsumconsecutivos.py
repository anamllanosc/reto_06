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
        print(f"Error: El numero de elementos debe ser un entero")

