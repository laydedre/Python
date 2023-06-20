'''Faça um Programa que peça 2 números inteiros e um número real.
Calcule e mostre:
● o produto do dobro do primeiro com metade do segundo .
● a soma do triplo do primeiro com o terceiro.
● o terceiro elevado ao cubo.'''

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite um número inteiro: "))
n3 = float(input("Digite um número real: "))

dobro = ((n1 * 2) * (n2/2))
soma = (n1 * 3) + n3
cubo = n3**3

print("Dobro do primeiro com metade do segundo:",dobro)
print("Soma do triplo do primeiro com o terceiro:",soma)
print("Terceiro elevado ao cubo:",cubo)