#!/usr/bin/env python
#Autor: Edward Ramos
#Date: 09/28/2016

ganho_por_hora = float(input("Insira o valor ganho por hora: "))
horas_trabalhadas = float(input("Insira o valor de horas trabalhadas:  "))

salario_b = (ganho_por_hora * horas_trabalhadas)

imp_renda = (salario_b * 0.11)
inss = (salario_b * 0.08)
sind = (salario_b * 0.05)

desconto = (imp_renda + inss + sind)
sal_liquido = (salario_b - desconto)

print("(+) Salario bruto: %r") % (salario_b)
print("DESCONTOS MENSAIS")
print(" Imposto de renda: %r") % (imp_renda)
print(" INSS: %r") % (inss)
print(" Sindicato: %r") % (sind)
print("(+) Valor total dos descontos: %r") % (desconto)
print("(+) Salario liquido: %r") % (sal_liquido)
