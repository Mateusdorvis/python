import tkinter as tk
import os
from model.model import UsuarioModel
from view.user_v import UsuarioView
from controller.controller import UsuarioController


os.system('cls')
if __name__ == "__main__":
    #este é o codigo principal e tmabém este modulo é principal
    root = tk.Tk()
    root.title("Gerenciamento de Usuários")
    root.geometry("400x300")

    model = UsuarioModel() #
    view = UsuarioView(root) #
    controller = UsuarioController(view, model)

    root.mainloop()
    model.fechar_conexao()