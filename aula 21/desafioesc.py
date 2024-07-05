import tkinter as tk
from tkinter import ttk

windows = tk.Tk()
windows.title("Desafio do esc")
windows.geometry("400x400")

msg = tk.Label(windows, text="desafio 1")
msg.pack()

def eventos_esc(event):
     print("Você apertou no F5")
     msg.config(text="Você apertou no F5")

btn = tk.Button(windows, text="clique em mim")
btn.bind("<Return>", eventos_esc)


btn.focus()
btn.pack(expand=True) # a ordem não importa, o que importa é que todo vez que fazer um comando utiliza focus

windows.mainloop()