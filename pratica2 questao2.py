# Faça uma função que receba uma lista como parâmetro e retorne somente os números pares da lista.

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lista2 = []
    
def pares():
    
    for i in lista1:
        if i % 2 == 0:
            lista2.append(i)

pares()
print(lista2)