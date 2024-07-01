import tkinter as interface
from casa import Casa

#o que eu quero que aconteça antes do mainloop

principal = interface.Tk()
principal.title("Informações do usuario")
principal.geometry("480x360")
casa = Casa()

entrada = interface.Entry(principal)

principal.mainloop()
