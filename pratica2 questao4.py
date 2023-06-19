# Faça uma função que computa a potência ab para valores a e b(assuma números inteiros) passados por parâmetro.

def funcao ():
    base = int(input("Digite a base: "))
    expoente = int(input("Digite o expoente: "))
    x = 1
    
    for x in range(1):
        x =  base ** expoente
        print(base, "elevado a", expoente, "=", x)
        
funcao()