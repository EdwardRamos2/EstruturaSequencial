#!/usr/bin/env python

#Faca um Programa que peca o raio de um circuloc calcule e mostre sua area

are_circulo = float(input("Insert value do diametro do circulo: \n'"))
print("value insert circulo diametro: %r") % (are_circulo)

are_circulo /= 2 #Divide o valor diametro
metade = (are_circulo) #are diametro dividida
pi = float(3.15)
are = float(metade * pi) #36 multi o valor de pi
print( "valor diametro divi: %r") % (metade)
print(" valor de pi: %r  ") % (pi)
print("are do circulo: %r ") % (are)


