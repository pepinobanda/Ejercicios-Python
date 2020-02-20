def areaCircle(radio):
  pi=3.1416
  area=float (pi) * int (radio) ** 2.0
  print("El área es: " + str (area))

print ("CALCULAR EL AREA DE UN CIRCULO")
radio1=input("CUAL ES EL RADIO: ")
areaCircle(radio1)
