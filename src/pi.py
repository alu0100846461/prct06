#! /usr/bin/python
#!encoding: UTF-8

#Importamos la librería sys para permitir el uso de sys.argv.
import sys 

#Almacenamos el valor de referencia de pi con 35 decimales.
PI = 3.1415926535897931159979634685441852

#Inicializamos una lista vacía.
lista = []

#Declaramos una función destinada a calcular el valor aproximado del número pi.
def f (n):
    suma = 0.0
    for i in range (1, n+1):
        xi = (i-0.5)/n
        fxi = 4/(1+xi**2)
        suma += fxi
    pi = suma/n 
    return pi

       #Cuerpo principal del programa

# Comprobamos que el usuario haya introducido como argumentos el número inicial de intervalos
# y las ejecuciones deseadas del algoritmo, y en caso contrario, lo solicitamos por pantalla.
if (len(sys.argv) == 1):
    n = int(raw_input("Introduzca el número de intervalos utilizados para aproximar pi: "))
    t = int(raw_input("Introduzca el número de ejecuciones del algoritmo: "))
elif (len(sys.argv) == 2):
    n = int(sys.argv[1])
    t = int(raw_input("Introduzca el número de ejecuciones del algoritmo: "))
else: 
    n = int(sys.argv[1])
    t = int(sys.argv[2])

#Si el número de intervalos es nulo o negativo, pedimos al usuario un reintento hasta obtener una respuesta válida.
while (n <= 0):
    n = int(raw_input("Debe introducir una cantidad positiva de intervalos. Inténtelo de nuevo: "))
while (n <= 0):
    t = int(raw_input("Debe introducir una cantidad positiva de ejecuciones. Inténtelo de nuevo: "))

print "Iteración\tValor obtenido\tValor real\tError cometido"
for j in range (1, t+1):
    pi = f(j*n)
    lista = lista + [pi]
    print "%d\t\t%1.10g\t%1.10g\t%1.10f" %(j, pi, PI, abs(pi-PI))
