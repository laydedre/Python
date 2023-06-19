# Pesquise e desenvolva uma função com a palavra reservada pass.

def palavra_reservada():
    num = 2
    for num in range(10):
        if num == 5:
            pass
        print("Numero é: " + str(num))

print(palavra_reservada())
print("FIM")