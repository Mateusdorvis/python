import tkinter as tk
from tkinter import messagebox

def mostrar_aviso():
    messagebox.showinfo("Aviso", "Esta é uma mensagem de aviso!")

# Criar a janela principal
janela = tk.Tk()
janela.title("Exemplo de Janela de Aviso")

# Botão para mostrar o aviso
botao = tk.Button(janela, text="Mostrar Aviso", command=mostrar_aviso)
botao.pack(pady=20)

# Executar o loop principal da janela
janela.mainloop()