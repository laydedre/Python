#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

prod1 = float(input("Digite o preço de um produto: "))
prod2 = float(input("Digite o preço de um produto: "))
prod3 = float(input("Digite o preço de um produto: "))

if (prod1<prod2 and prod1<prod3):
    menor = prod1
    print("O maior número entre os que foram inseridos é: ",menor)

if (prod2<prod1 and prod2<prod3):
    menor = prod2
    print("O maior número entre os que foram inseridos é: ",menor)

if (prod3<prod1 and prod3<prod2):
    menor = prod3
    print("O maior número entre os que foram inseridos é: ",menor)