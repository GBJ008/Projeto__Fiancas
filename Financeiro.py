import time

#entrada
ValoresEntrada= []
Valores_despesa_fixa = []
Valores_despesa_variavel = []


nome = input('Por favor nós informe seu nome: ')
print(f'Olá {nome}, seja bem vinda a sua planilha finaceira')
print('Vamos começar!!!')

time.sleep(0.50)
#Valores de entradas 

tem_mais_1entrdas= input('Tem mais de uma entrada esss mês? Sim ou Não ').upper()
print('Beleza, vamos lá...')

def despesas():
 if tem_mais_1entrdas == 'SIM':


    quantidade_entrada = int(input('Digite a quantidade: '))

    for i in range (quantidade_entrada):
        valor= float(input('Digite os valores que foram recebidos: '))
        ValoresEntrada.append(valor)

 elif tem_mais_1entrdas == 'NÃO':
   valor= float(input('Digite o valor que foi recebido: '))
   ValoresEntrada.append(valor)


#valores de despesas fixas
print(40*'_')

Tem_despesas_fixa = input('E de despesas fixas tem mais de uma? Sim ou Não ').upper()

def depesaFixa():
 if Tem_despesas_fixa == 'SIM':
    QuantidadeFixa = int(input('Digite a quantidade de despesas fixas: '))

    for i  in range (QuantidadeFixa):
     valor= float(input('Digite o valor das despesas fixas: '))
     Valores_despesa_fixa.append(valor)

 elif Tem_despesas_fixa == 'NÃO':
    Valor = float(input('Digite o valor de despesa fixa: '))
    Valores_despesa_fixa.append(valor)


print(40*'_')
# Valores de entradas variaveis

Mais_entrada_variaveis = input('tem mas de uma despesas váriavel? Sim ou Não ').upper()]

def despesaVariavel():
 if Mais_entrada_variaveis == 'SIM':
    quantidade_variavel = int(input('Quantas despesas váriavel: '))

    for i in range (quantidade_variavel):
     valor = float(input('Digite o valor das despesas variável: '))
     Valores_despesa_variavel.append(valor)

 elif Mais_entrada_variaveis == 'NÃO':
    valor = float(input('Digite o valor da despesa variável: '))
    Valores_despesa_variavel.append(valor)

# total de tudo/soma
total_entrada = sum(ValoresEntrada)
total_despesas_fixa= sum(Valores_despesa_fixa)
total_variaveis = sum(Valores_despesa_variavel)
Total_Despesas_fixa_variavel = total_despesas_fixa + total_variaveis
total_valores_sub = total_entrada - Total_Despesas_fixa_variavel

if total_valores_sub <= 0:
    print('Cuidado você está gastando de mais!!!!')
else:
    print('parabéns está tudo em ordem!!!!')

print(10*' ')
print(f'o total de valores de entradas é R${total_entrada:.2f}')
print(10*' ')
print(f'E o total de Despesas fixas é R${total_despesas_fixa:.2f}')
print(10*' ')
print(f'e o total de despesas variáveis R${total_variaveis:.2f} ')
print(10*' ')
print(f'o valor final que irá sobrar é R${total_valores_sub:.2f} no final do mês')

# Abertura de arquivos para arquivo texto
AberturaArquivo = open('dados.txt' , 'w')
# Escrita
AberturaArquivo.write(f'Seja bem vindo {nome} a sua tabela.\n')
print(' \n')
AberturaArquivo.write(f'Valores de entrada          Despesas fixas          Despesas Variáveis\n')
print(' \n')
AberturaArquivo.write(f'R${total_entrada:<10}            R${total_despesas_fixa:<10}         {total_variaveis:<10}\n')
print(' \n')
AberturaArquivo.write(f'e iram te sobrar final do mês                                 {total_valores_sub:.2f}\n')

AberturaArquivo.close()