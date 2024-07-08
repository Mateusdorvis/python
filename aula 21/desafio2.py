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
main.mainloop()