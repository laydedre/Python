# Faça uma função que peça dois números como parâmetro e mostre na tela o resultado das 4 operações matemáticas.

def operacao ():
    a = float(input("Primeiro número:  "))
    b = float(input("Segundo número:  "))
    c = input("Digite a operação a realizar + - * / :   ")
    
    if c == "+":
        num = a + b
        print(num)
        
    elif c == "-":
        num = a - b
        print(num)
    
    elif c == "*":
        num = a * b
        print(num)
    
    elif c == "/":
        num = a / b
        print(num)
    
    else:
        print("Digite uma operação indicada!")

operacao()