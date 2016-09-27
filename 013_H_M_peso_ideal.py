#!/usr/bin/env python
#Autor: Edward Ramos
#Date: 09/26/2016

#Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes formulas:
"""
    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7 (h = altura)

"""
print("PESO IDEAL:")

opcao1 = int(input("Digite (1 -Homem)  ou (2 Mulher)"))

if opcao1 == 1:
    def peso_ideal():
        if 1 == 1:
            altura = float(input("Digite sua altura:"))
            if altura != 0:
                print("(+) Altura inserida com sucesso:\n")
                peso = (72.7 * altura) - 58
                peso1 = float(peso)

                print("Sexo escolhido: (1- Homem)")
                print("Seu peso ideal e: %r") % (peso1)
            else:
                print("(+) Sucesso")
        else:
            print("(+) Sucesso2")
    print (peso_ideal())
else:
    print("(+) ok")

if opcao1 == 2:
    def peso_ideal2():
        if 2 == 2:
            altura2 = float(input("Digite sua altura:"))
            if altura2 != 0:
                print("(+) Altura inserida com sucesso:\n")
                peso3 = (62.1 * altura2) - 44.7

                print("Sexo escolhido: (2 Mulher)")
                print("Seu peso ideal e: %r") % (peso3)
            else:
                print("OK")
        else:
            print("OK")
    print (peso_ideal2())
else:
    print("(+) ok")


