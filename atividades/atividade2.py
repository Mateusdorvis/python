import tkinter as tk
from tkinter import ttk
principal = tk.Tk()
principal.title("clique")

msg = tk.Label(principal, text="Texto")
msg.pack(side="top")
click = 0


def conta_click():
    global click
    click+=1
    msg.config(text=f"Você clicou {click}")

def button_remover():
    global click
    click-=1
    msg.config(text=f"Você removeu {click}")


botao = tk.Button(principal, text="clique aqui", command=conta_click)
botao.pack(side="top")

botao_remover = tk.Button(principal, text="Clique para remover", command=button_remover)
botao_remover.pack(side="top")
principal.mainloop()

