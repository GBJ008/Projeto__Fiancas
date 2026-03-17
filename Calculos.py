#entrada
ValoresEntrada= []
ValoresDespesas = []

for entrada in range(3):
    valor= float(input('Digite os valores que foram recebidos: '))
    ValoresEntrada.append(valor)

print(40*'_')
for depesa in range(3):
    valor= float(input('Digite os valores de gastos deess mês: '))
    ValoresDespesas.append(valor)

total_entrada = sum(ValoresEntrada)
total_despesas = sum(ValoresDespesas)

total_valores_sub = total_entrada - total_despesas

print(f' o total de valores de entradas é R${total_entrada:.2f}\n E o total de Despesas é R${total_despesas:.2f}')
print(f'o valor fianl que irar sobrar é R${total_valores_sub} no final do mês')