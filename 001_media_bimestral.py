#Faca um Programa que peca as 4 notas bimestrais e mostre a media.

nota1 = int(input("Insert primeira nota bimestral"))
nota2 = int(input("Insert segunda nota bimestral"))
nota3 = int(input("Insert terceira nota bimestral"))
nota4 = int(input("Insert quarta nota bimestral"))

soma = (nota1 + nota2 + nota3 + nota4)
valor_medio = (soma)
soma /= 4
print ("Valores do bimestre, nota1 %d nota2 %d nota3 %d nota4 %d \n'") % (nota1,nota2,nota3,nota4)
print ("Valor soma: %d ") % (int(valor_medio))
print("Valor medio: %d\n'") % (soma)
