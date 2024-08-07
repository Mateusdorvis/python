import tkinter as tk
from tkinter import ttk
from view.user_v import UsuarioView
from model.model import UsuarioModel

class UsuarioController:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.view.adicionar_button.config(command=self.adicionar_usuario)
        self.carregar_usuarios()

    def adicionar_usuario(self):
        nome = self.view.get_nome()
        idade = self.view.get_idade()
        if nome and idade.isdigit():
            self.model.inserir_usuario(nome, int(idade))
            self.view.adicionar_usuario_lista((None, nome, idade))
            self.view.nome_entry.delete(0, tk.END)
            self.view.idade_entry.delete(0, tk.END)

    def carregar_usuarios(self):
        usuarios = self.model.selecionar_usuarios()
        id_number = self.model.selecionar_id()
        for usuario, ids in usuarios, id_number:
            self.view.adicionar_usuario_lista(usuario, ids)
            

            

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gerenciamento de Usuários")
    root.geometry("400x300")

    model = UsuarioModel()
    view = UsuarioView(root)
    controller = UsuarioController(view, model)

    root.mainloop()
    model.fechar_conexao()