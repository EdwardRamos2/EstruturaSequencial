#!/usr/bin/env python
#*-*coding: utf-8 *-*
#Autor: EdwardRamos

# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit. 

c = float(input("Insert value in Celsius:"))

f = (c * 1.8000) + 32

print("Value convert in Fahrenheit: %r") % float(f)
