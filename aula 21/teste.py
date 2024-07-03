import tkinter as tkt
from tkinter import ttk

main = tkt.Tk()
main.title("teste")
main.geometry("500x500")

label1 = tkt.Label(main, text="Sou label 1", font="Arial", background="red")
label2 = tkt.Label(main, text="Sou label 2", font="Arial", background="orange")

label1.grid(row=1, column=0)
label2.grid(row=1, column=2)

main.mainloop()