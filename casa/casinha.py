import tkinter as interface
from tkinter import ttk
from casa1 import Casa

#o que eu quero que aconteça antes do mainloop

principal = interface.Tk()
principal.title("Informações do usuario")
principal.geometry("480x360")
casa = Casa("Laranja", 42, "Rua 2022 - Mario Quinatana, Porto Alegre", "Mateus", 8, 8, 5
)

#cor da casa
mensagem = interface.Label(principal, text=casa.cor_da_casa_externo, fg="orange", justify="center")
mensagem.pack(side="left", fill="both")
#numero da casa
mensagem2 = interface.Label(principal, text=casa.numero_da_casa)
mensagem2.pack(side="left", fill="both")
#endereco
mensagem3 = interface.Label(principal, text=casa.endereco)
mensagem3.pack(side="left", fill="both")
#proprietario
mensagem4 = interface.Label(principal, text=casa.propreitario)
mensagem4.pack(side="left", fill="both")
#numero de comodos
mensagem5 = interface.Label(principal, text=casa.numer_janelas)
mensagem5.pack(side="left", fill="both")
#numero de portas
mensagem6 = interface.Label(principal, text=casa.porta)
mensagem6.pack(side="left", fill="both")
#numero de comodos
mensagem7 = interface.Label(principal, text=casa.comodo)
mensagem7.pack(side="left", fill="both")

principal.mainloop()
