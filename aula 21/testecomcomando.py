import tkinter as tk
from tkinter import ttk

def return_pressed(nada): #o BIND necessita de parâmetro, se tirar o codigo quebra
    print('Você clicou na tecla enter')


root = tk.Tk()

btn = ttk.Button(root, text='Save',command= lambda : print('Você clicou a tecla space') )
btn.bind('<Return>', return_pressed)


btn.focus()#precisa do focus para manter o botão em foco e ler o bind() dele
btn.pack(expand=True)



root.mainloop()
