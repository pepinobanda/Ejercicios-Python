import random
def comparar(nu):
    numale=random.randrange(10)
    if(nu > numale):
        print("El número mayor es el ingresado por el usuario: " + str (nu))
        print("Numero RANDOM: " + str(numale))
    if(nu < numale):
        print("El número mayor es el RANDOM: " + str (numale))
        print("Numero usuario: " + str(nu))
    if(nu == numale):
        print("Los dos números son iguales: " + str (numale) +" " + str (nu))
        
print ("INGRESE NÚMERO 1-10")
numero=input("¿CUÁL ES SU NÚMERO?: ")
comparar(int(numero))
