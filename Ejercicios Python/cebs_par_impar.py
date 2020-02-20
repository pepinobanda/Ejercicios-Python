def numparinpar(num):
    num = int(num)
    if((num%2) == 0):
        print("El numero " + str(num) + " es par.")
    else:
        print("El numero " + str(num) + " es inpar.")
print ("CALCULAR NUMERO PAR - INPAR")
numero=input("¿CUÁL ES SU NÚMERO?: ")
numparinpar(numero)
