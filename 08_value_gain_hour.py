#!/usr/bin/env python
#Faca um Programa que pergunte quanto voce ganha por hora
#e o numero de horas trabalhadas no mes.
# Calcule e mostre o total do seu salario no referido mes.

value_time = float(input("Quanto voce granha por hora?, please insert valor:  "))
mes = raw_input("Mes origem:  ")
horas = float(input("Quantas horas trabalhadas no mes?:  "))

bruto = (value_time * horas)

print("Valor ganho por hora: %r") % (value_time)
print("Mes de origem: %s") % (mes)
print("Total de horas: %r") % (horas)
print("Valor total por mes: %r$ reais") % (bruto)
