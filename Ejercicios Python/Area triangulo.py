def calcuAreaTri(b,a):
    area=int (b) * int (a) / 2.0
    print ("El área es: " + str (area))

print ("CALCULAR EL AREA DE UN TRIANGULO")
base=input("CUAL ES LA BASE: ")
altura=input("CUAL ES LA ALTURA: ")
calcuAreaTri(base,altura)
