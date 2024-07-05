import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("canvas")

grafico = tk.Canvas(janela, width=450, height=450, bg="#13a60e")
grafico.pack()

grafico.create_rectangle(90,90 ,190 ,190 , fill="#050000")#create_rectangle(x0,y0, x1, y0) x = vertical y = horizontal

grafico.create_rectangle(290,90, 390, 190 , fill="red")
grafico.pack()

#nariz
grafico.create_rectangle(191,191, 290,350 , fill="blue")
grafico.pack()

#nariz do lado esquerdo
grafico.create_rectangle(290,250,390,350 , fill="yellow")
grafico.pack()

#nariz lado direito
grafico.create_rectangle(290,250,390,350 , fill="yellow")
grafico.pack()






janela.mainloop()