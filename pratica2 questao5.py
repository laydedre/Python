# Escreva uma função que, dado o valor da conta de um restaurante, calcule e exiba a gorjeta do garçom, considerando 10% do valor da conta.

def valor_conta(valor):
    gorjeta = 0.10 * valor
    print("Total a ser pago ao garçom: R$", gorjeta)

valor_conta(200)