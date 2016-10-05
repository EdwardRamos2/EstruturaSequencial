#!/usr/bin/env python
#*-*coding: utf-8 *-*
#Autor: EdwardRamos

# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
#usando a seguinte fórmula: (72.7*altura) - 58 

print("(+)     Your ideal weight!!!!!")
height = float(raw_input("Enter your height: "))
if height != 0:
    print("(+)  ok ")
    weight = (72.7 * height) - 58
    print("You ideal weight: %r") % (weight)
