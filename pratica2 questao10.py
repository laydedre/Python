# Pesquise e desenvolva uma função com valores padrões.

def soma(a, b=10):  # foi definido o valor 10 como padrão de b. Caso não seja fornecido pelo programa a função usará esse valor
    s = a + b 
    return s

print(soma(7)) #usará o valor padrão

print(soma(7, 3)) #nesse caso usará o 3 como o valor de b