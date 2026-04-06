import customtkinter as ctk
from tkinter import *
import pandas as pd

#configuração de aparencia
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')

#configuração de janela
app = ctk.CTk()
app.title('Finaças')
app.geometry('600x600')


#entrada de dados
ValoresEntrada= []
Valores_despesa_fixa = []
Valores_despesa_variavel = []


#funcoes
def despesasFixas():
    def cmdDespesaFixa():
        despesaFixa = int(entDespesaFixa.get())
        lblDespesaFixa.destroy()
        entDespesaFixa.destroy()
        btnDespesaFixa.destroy()
        
        def vlrEntrada():
            valorDespesa = float(entValorDespesa.get())
            Valores_despesa_fixa.append(valorDespesa)
            entValorDespesa.delete(0, END)
            entValorDespesa.focus()
            if despesaFixa == len(Valores_despesa_fixa):
                lblValorDespesa.destroy()
                entValorDespesa.destroy()
                btnValorDespesa.destroy()
                despesasVariaveis()
        
        lblValorDespesa = ctk.CTkLabel(app,text='Quais valores das suas despesas?')
        lblValorDespesa.pack(pady=10)
            
        entValorDespesa = ctk.CTkEntry(app, placeholder_text='Valor das despesas fixas', width=150)
        entValorDespesa.pack(pady=10)
        entValorDespesa.focus()
            
        btnValorDespesa = ctk.CTkButton(app, text='Adicionar valor', command=vlrEntrada, width=150)
        btnValorDespesa.pack(pady=10)

    #criação de campos
    lblDespesaFixa = ctk.CTkLabel(app,text='Quantas despesas você teve esse mês?')
    lblDespesaFixa.pack(pady=10)

    entDespesaFixa = ctk.CTkEntry(app, placeholder_text='Despesas fixas', width=150)
    entDespesaFixa.pack(pady=10)
    entDespesaFixa.focus()

    btnDespesaFixa = ctk.CTkButton(app, text='Adicionar despesas', command=cmdDespesaFixa, width=150)
    btnDespesaFixa.pack(pady=10)
    
    
def despesasVariaveis():
    def cmdDespesaVariavel():
        despesaVariavel = int(entDespesaVariavel.get())
        lblDespesaVariavel.destroy()
        entDespesaVariavel.destroy()
        btnDespesaVariavel.destroy()
        
        def vlrEntrada():
            valorDespesaVariavel = float(entValorDespesaVariavel.get())
            Valores_despesa_variavel.append(valorDespesaVariavel)
            entValorDespesaVariavel.delete(0, END)
            entValorDespesaVariavel.focus()
            if despesaVariavel == len(Valores_despesa_variavel):
                lblValorDespesaVariavel.destroy()
                entValorDespesaVariavel.destroy()
                btnValorDespesaVariavel.destroy()
                calculosTotais()
        
        lblValorDespesaVariavel = ctk.CTkLabel(app,text='Quais valores das suas despesas?')
        lblValorDespesaVariavel.pack(pady=10)
            
        entValorDespesaVariavel = ctk.CTkEntry(app, placeholder_text='Valor das despesas variavel', width=150)
        entValorDespesaVariavel.pack(pady=10)
        entValorDespesaVariavel.focus()
            
        btnValorDespesaVariavel = ctk.CTkButton(app, text='Adicionar valor', command=vlrEntrada, width=150)
        btnValorDespesaVariavel.pack(pady=10)

    #criação de campos
    lblDespesaVariavel = ctk.CTkLabel(app,text='Quantas despesas variaveis você teve esse mês?')
    lblDespesaVariavel.pack(pady=10)

    entDespesaVariavel = ctk.CTkEntry(app, placeholder_text='Despesas varivavel', width=150)
    entDespesaVariavel.pack(pady=10)
    entDespesaVariavel.focus()
    
    btnDespesaVariavel = ctk.CTkButton(app, text='Adicionar despesas', command=cmdDespesaVariavel, width=150)
    btnDespesaVariavel.pack(pady=10)


def entradaValores():
    def cmdQtdEntrada():
        qtdEntrada = int(entQtdEntrada.get())
        lblQtdEntrada.destroy()
        entQtdEntrada.destroy()
        btnQtdEntrada.destroy()
        
        def vlrEntrada():
            valorEntrada = float(entValorEntrada.get())
            ValoresEntrada.append(valorEntrada)
            entValorEntrada.delete(0, END)
            entValorEntrada.focus()
            if qtdEntrada == len(ValoresEntrada):
                lblValorEntrada.destroy()
                entValorEntrada.destroy()
                btnValorEntrada.destroy()
                despesasFixas()
        
        lblValorEntrada = ctk.CTkLabel(app,text='Quais valores você recebeu?')
        lblValorEntrada.pack(pady=10)
            
        entValorEntrada = ctk.CTkEntry(app, placeholder_text='Entradas mensal', width=150)
        entValorEntrada.pack(pady=10)
        entValorEntrada.focus()
            
        btnValorEntrada = ctk.CTkButton(app, text='Adicionar valor', command=vlrEntrada, width=150)
        btnValorEntrada.pack(pady=10)

    #criação de campos
    lblQtdEntrada = ctk.CTkLabel(app,text='Quantas entradas você teve esse mês')
    lblQtdEntrada.pack(pady=10)

    entQtdEntrada = ctk.CTkEntry(app, placeholder_text='Entradas mensal', width=150)
    entQtdEntrada.pack(pady=10)
    entQtdEntrada.focus()

    btnQtdEntrada = ctk.CTkButton(app, text='Adicionar entradas', command=cmdQtdEntrada, width=150)
    btnQtdEntrada.pack(pady=10)

def calculosTotais():
    total_entrada = sum(ValoresEntrada)
    total_despesas = sum(Valores_despesa_fixa)
    total_valores_sub = total_entrada - total_despesas
    total_variaveis = sum(Valores_despesa_variavel)

    textbox = ctk.CTkTextbox(app, width=450, height=200, border_spacing=20)
    textbox.pack(pady=30)
    if total_valores_sub >= 0:
        texto = (
            f"Parabéns, está tudo em ordem \n\n"
            f"• O total de valores de entradas é R${total_entrada}\n\n"
            f"• E o total de Despesas é R${total_despesas}\n\n"
            f"• O valor final que irá sobrar é R${total_valores_sub} no final do mês\n\n"
            f"• Você tem o total de R${total_despesas} de despesas fixas, e R${total_variaveis} de despesas variáveis."
        )
    else:
        texto = (
            f"Cuidado você está gastando demais \n\n"
            f"• O total de valores de entradas é R${total_entrada}\n\n"
            f"• E o total de Despesas é R${total_despesas}\n\n"
            f"• O valor final que irá sobrar é R${total_valores_sub} no final do mês\n\n"
            f"• Você tem o total de R${total_despesas} de despesas fixas, e R${total_variaveis} de despesas variáveis."
        )
    textbox.insert("0.0", texto)    
    
    
entradaValores()

app.mainloop()