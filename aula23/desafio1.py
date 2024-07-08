import tkinter as tk
from tkinter import ttk
import os

os.system('cls')
principal = tk.Tk()
principal.title("Coletando dados do usuário")
#função para realizar perguntas 

def coleta_dados_para_mim():
        #pergunta para o 
    def nome_do_usuario():
        nome= tk.Label(principal, text="Digite seu nome completo:")
        nome.pack()
        nome_entrada = tk.Entry(principal, width=20)
        nome_entrada.pack()
    nome_do_usuario()
    #pergunta a idade

    def idade_do_usuario():
        idade = tk.Label(principal, text="Digite sua idade :")
        idade.pack()
        idade_entrada = tk.Entry(principal, width=20)
        idade_entrada.pack()
    idade_do_usuario()

crollbar = ttk.Scrollbar(principal, orient='vertical', command=coleta_dados_para_mim)
crollbar.pack(side="left", expand=True)

    
coleta_dados_para_mim()

principal.mainloop()