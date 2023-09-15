#Vamos a crear un codigo que realice por panatalla un calculo de variables, que nospermita sumar
#restar y hacer operaciones para mostrar al final un resultado e cada operacion y a su vez crear una tabla de
#la verdad y cada una de las operaciones usando "bool o usando and y or"
print ("Este programa no se debe hacer por chatGPT el que lo haga le bajo nota")

a = input ("Deme un número en panatalla: ")
b = input ("Deme un número mayor que el anterior: ")

a = int(a)
b = int(b)

print (a+b)
print (a-b)
print (a*b)
print (a/b)
print (a%b)

print ("Tabla de verdad todo lo relacionado con And o Y")

print ((str(a==a)) + " and " + str (a==a) + " ----> " + str (a==a))
print ((str(a==a)) + " and " + str (a==b) + " ----> " + str (a==b))
print ((str(a==b)) + " and " + str (a==a) + " ----> " + str (a==b))
print ((str(a==b)) + " and " + str (a==b) + " ----> " + str (a==a))

print (bool(a==a))
print (bool(a==b))
