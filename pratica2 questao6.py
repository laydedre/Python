# Pesquise e desenvolva uma função sobre o parâmetro *args.

def adicional_vendas(salario, *args):
    total_vendas = 0
    for i in args:
        total_vendas += salario * i
    return total_vendas

print(adicional_vendas(1400, 0.10, 0.50))