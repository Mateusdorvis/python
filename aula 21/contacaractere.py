import tkinter as t
import os
from tkinter import ttk
os.system('cls')
main = t.Tk()
label = t.Label(main, text="digite algo")
label.pack()
#gerar um container (widget)
texto = t.Text(main, font="Arial")
texto.pack()

#teste sem def
def verifica(verifica):
    msg = t.Label(main)
    pegue_o_texto = texto.get('1.0','22.0')
    leitura = len(pegue_o_texto)
    if leitura>20:
        texto['state'] = 'disabled'
        msg.config(text="ultrapassou")
        msg.pack()
        print("ultrapassou")
        
    else:
        msg.config(text="continue escrevendo")
        msg.pack()
        print("continue escrevendo")

    

# realizar <KeyRealase>
texto.bind("<KeyRelease>", verifica)

main.mainloop()
print("terminou")