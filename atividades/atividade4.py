import tkinter as tk
from tkinter import ttk

principal = tk.Tk()
principal.title("atividade 4")
principal.geometry("600x500")

nome = tk.Label(principal, text="Digite seu nome completo")
nome.pack()

entrada1 = tk.Entry(principal, width=50)
entrada1.pack(side="top")


data = tk.Label(principal, text="Digite sua data de nascimento completo")
data.pack()

entrada2 = tk.Entry(principal, width=50)
entrada2.pack(side="top")

def enviar():
    entrada_de_dados_name= entrada1.get()
    entrada_de_dados_nascimento = entrada2.get()
    dado_completo = tk.Label(principal, text="Obrigado por transfirir suas informações")
    dado_completo.pack(side="top")
    dicio_dados = {
        "Nome completo do usuário cadastrado " : entrada_de_dados_name ,
        "Data de nascimento completo do usuário cadastrado" : entrada_de_dados_nascimento
    }
    for a  in dicio_dados.items():
        print(a)

botao = tk.Button(principal, text="enviar os dados", command=enviar)
botao.pack(side="top")
principal.mainloop()



