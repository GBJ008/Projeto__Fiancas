#entrada
ValoresEntrada= []
Valores_despesa_fixa = []
Valores_despesa_variavel = []


quantidade_entrada = int(input('Quantas entradas você tem esse mês: '))
print(10*' ')
quantidade_despesas_fixa = int(input('quantas despesas fixa você tem: '))
print(10*' ')
quantidade_despesas_variavel = int(input('quantas depesas variável você tem: '))

for entrada in range(quantidade_entrada):
    valor= float(input('Digite os valores que foram recebidos: '))
    ValoresEntrada.append(valor)

print(40*'_')
for despesa in range(quantidade_despesas_fixa):
    valor= float(input('Digite o valor das despesas fixas: '))
    Valores_despesa_fixa.append(valor)

for despesa in range(quantidade_despesas_variavel):
    valor = float(input('Digite o valor das despesas variável:'))
    Valores_despesa_variavel.append(valor)


# total de tudo
total_entrada = sum(ValoresEntrada)
total_despesas = sum(Valores_despesa_fixa)
total_valores_sub = total_entrada - total_despesas
total_fixa = sum(Valores_despesa_fixa)
total_variaveis = sum(Valores_despesa_variavel)
if total_valores_sub <= 0:
    print('Cuidado você está gastando de mais')
else:
    print('parabéns está tuo em ordem')

print(f'o total de valores de entradas é R${total_entrada:.2f}')
print(10*' ')
print(f'E o total de Despesas é R${total_despesas:.2f}')
print(10*' ')
print(f'o valor final que irá sobrar é R${total_valores_sub} no final do mês')
print(10*' ')
print(f'você tem o total de {total_fixa} de despesas fixas, e tem {total_variaveis} de despesas váriaveis.')
