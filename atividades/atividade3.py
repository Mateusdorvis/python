import tkinter as tk
from tkinter import ttk

principal = tk.Tk()
principal.title("atividade 3")

msg = tk.Label(principal, text="Texto")
msg.pack(side="right")


def texto_alterado():
    msg.config(text="Você alterou o texto")

entrada = tk.Entry(principal, width=10 )
entrada.pack(pady=10, side="right")

botao = tk.Button(principal, text="clique aqui", command=texto_alterado)
botao.pack(anchor="center")
principal.mainloop()