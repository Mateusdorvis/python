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
mensagem = interface.Label(principal, text=f"Cor da casa :{casa.cor_da_casa_externo}", fg="white", background="#ff823a")
mensagem.pack(side="top", fill="both")

mensagem2 = interface.Label(principal, text=f"numero da casa :{casa.numero_da_casa}", fg="white", background="#b9030f")
mensagem2.pack(side="top", fill="both")

mensagem3 = interface.Label(principal, text=f"Endereço da casa :{casa.endereco}",  fg="white", background="#95cfb7")
mensagem3.pack(side="top", fill="both")

mensagem4 = interface.Label(principal, text=f"Propriedade da casa :{casa.propreitario}",  fg="white", background="#ffab07")
mensagem4.pack(side="top", fill="both")

mensagem5 = interface.Label(principal, text=f"Numero de janelas da casa :{casa.numer_janelas}",  fg="white", background="#161917")
mensagem5.pack(side="top", fill="both")

mensagem6 = interface.Label(principal, text=f"Numero de portas da  casa :{casa.porta}",  fg="white", background="#473469")
mensagem6.pack(side="top", fill="both")

mensagem7 = interface.Label(principal, text=f"Numero de comodos da casa :{casa.comodo}",  fg="white", background="#4c5e91")
mensagem7.pack(side="top", fill="both") 



principal.mainloop()
