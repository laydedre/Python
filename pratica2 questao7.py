# Pesquise e desenvolva uma função sobre o parâmetro **kwargs.

def adicional_vendas(salario, **kwargs):
    total_vendas = 0
    print(kwargs)
    if "percentual_10" in kwargs:
        total_vendas += salario * kwargs["percentual_10"]
    if "percentual_50" in kwargs:
        total_vendas += salario * kwargs["percentual_50"]
    return total_vendas

print(adicional_vendas(1400, percentual_10=0.10, percentual_50=0.50))