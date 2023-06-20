''' Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
● Para homens: (72.7*h) - 58
● Para mulheres: (62.1*h) - 44.7 '''

sexo = input("Digite as seguintes siglas para sexo, F - feminino e M - masculino: ")
h = float(input("Digite sua altura (EX: 1.50):  "))

m = (72.7 * h) - 58
f = (62.1 * h) - 44.7

if(sexo == "M" or sexo == "m"):
        print("O seu peso ideal é: ",m)

else:
        print("O seu peso ideal é: ",f)