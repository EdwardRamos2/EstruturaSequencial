#!/usr/bin/env python
#Autor: Edward Ramos
#Autor: 09/26/2016

print("####### PRODUCAO DE PEIXES #######")
print("De acordo com o regulamento de pesca do estado de SP")
print("Se o peso de peixes ultrapassar 50K")
print("deve ser pago 4 Reais por quilo excedente")
print("")
print("")
print("Ola, por favor insira a quantidade de peixes por Quilo:\n")

def peixes():
    quilo = float(input("Informe aqui o valor:  "))
    if quilo != 0:
        print("(+) Quilo inserido!\n")
    if quilo >= 50:
        sobra = (quilo - 50)
        multa = (sobra * 4)
        print("(+) Valor quilo informado: (%r)") % (quilo)
        print("(+) Valor excedente em quilos: (%r)") % (sobra)
        print("(+) Valor multa, por quilo excedente: (%r) Reais") % (multa)
    elif quilo <= 50:
       print("(+) Produto dentro do permitido")
       print("(+) Quilos informado: %r") % (quilo)
       print("(+) Nao havera multa")
    else:
         print("(+)")
print (peixes())
