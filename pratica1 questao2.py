# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))
nota4 = float(input("Digite sua quarta nota: "))

soma = (nota1 + nota2 + nota3 + nota4)
media = (soma/4)

print("A média foi:",media)