import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("canvas")

grafico = tk.Canvas(janela, width=450, height=450, bg="#13a60e", borderwidth=12, relief="solid")
grafico.pack()

grafico.create_rectangle(90, 100, 190, 200, fill="#050000")

grafico.create_rectangle(290, 100, 390, 200, fill="#050000")
grafico.pack()

grafico.create_rectangle(191, 200, 291, 300, fill="black")
grafico.pack()




janela.mainloop()