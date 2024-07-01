import tkinter as interface
from tkinter import ttk
from casa1 import Casa

#o que eu quero que aconteça antes do mainloop

principal = interface.Tk()
principal.title("Informações do usuario")
principal.geometry("480x360")
casa = Casa("none", "none", "none", "none", "none", "none", "none"
)
#cor da casa
mensagem = interface.Label(principal, text=casa.cor_da_casa_externo)
mensagem.pack(side="top", fill="both")
#numero da casa
mensagem2 = interface.Label(principal, text=casa.numero_da_casa)
mensagem2.pack(side="top", fill="both")
#endereco
mensagem3 = interface.Label(principal, text=casa.endereco)
mensagem3.pack(side="top", fill="both")
#proprietario
mensagem4 = interface.Label(principal, text=casa.propreitario)
mensagem4.pack(side="top", fill="both")
#numero de comodos
mensagem5 = interface.Label(principal, text=casa.numer_janelas)
mensagem5.pack(side="top", fill="both")
#numero de portas
mensagem6 = interface.Label(principal, text=casa.porta)
mensagem6.pack(side="top", fill="both")
#numero de comodos
mensagem7 = interface.Label(principal, text=casa.comodo)
mensagem7.pack(side="top", fill="both")

principal.mainloop()
