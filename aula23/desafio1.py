import tkinter as tk
from tkinter import ttk
import os


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

    def idade_do_usuario(event):
        idade = tk.Label(principal, text="Digite sua idade :")
        idade.pack()
        idade_entrada = tk.Entry(principal, width=20)
        idade_entrada.pack()
    idade_do_usuario
        
    

coleta_dados_para_mim()

principal.mainloop()