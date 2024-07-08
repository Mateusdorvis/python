#bota~o que reseta o texto


import tkinter as tk
from tkinter import ttk

main = tk.Tk()
main.title("desafio ")
main.geometry("500x500")
label = tk.Label(main, text="escreva algo na caixa de texto")
label.pack()

text = tk.Text(main)
text.pack()

def verificar(teclado):
    pega_o_texto = text.get("1.0", "22.0")
    if len(pega_o_texto)>20:
        text['state'] = 'disabled'
    else:
        mgs = tk.Label(main, text="continue escrevendo")
        mgs.pack()
text.bind("<KeyRelease>", verificar)
main.mainloop()