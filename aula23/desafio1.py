import tkinter as tk
from tkinter import ttk
import os

os.system('cls')
principal = tk.Tk()
principal.resizable(False, False)
principal.geometry('500x500')
principal.title("Coletando dados do usuário")

#funcao criada para reutilizar a funcao
class Funcao:
    def __init__(self, texto_string, linha1, linha2):
        self.texto_string = texto_string
        self.linha1 = linha1
        self.linha2 = linha2
        pass
   
    def perguntaAletoria(self, texto, linhalabel, linhaentrada):
         #label que dá informação
        pergunta = tk.Label(principal, text=texto)
        pergunta.grid(row=linhalabel, column=0, sticky='nsew')

        entrada_principal = tk.Entry(principal, width=20)
        entrada_principal.grid(row=linhaentrada, column=0, sticky='nsew')
        

#aqui nasce
funcao = Funcao("none", 0, 0)
#pergunta 1
funcao.perguntaAletoria("Digite seu nome completo abaixo :", 0, 1)
#pergunta 
funcao.perguntaAletoria("Digite sua idade abaixo :", 2, 3)
#pergunta 3
funcao.perguntaAletoria("Digite seu estado civil abaixo :", 4, 5)
#pergunta 4
funcao.perguntaAletoria("Digite cidade em que mora abaixo :", 6, 7)
#pergunta 5
funcao.perguntaAletoria("Digite bairro em que mora na sua cidade abaixo :", 8, 9)
#pergunta 6
funcao.perguntaAletoria("Digite  numero da casa em que mora abaixo :", 10, 11)
#pergunta 7
funcao.perguntaAletoria("Digite quantas pessoas mora com vocÊ abaixo :",12, 13)
#pergunta 8
funcao.perguntaAletoria("Digite sua série favorita abaixo :", 14, 15)
#pergunta 9
funcao.perguntaAletoria("Digite seu filme favorito civil abaixo :", 16, 17)
#pergunta 10
funcao.perguntaAletoria("Digite seu livro favorito abaixo :", 18, 19)
#pergunta 11
funcao.perguntaAletoria("Digite seu número do seu pé abaixo :", 20, 21)
#pergunta 12
funcao.perguntaAletoria("Digite quantos eletronicos você possui abaixo :", 22, 23)
#pergunta 13
funcao.perguntaAletoria("Digite quantos animais de estimação possui abaixo :", 24, 25)
#pergunta 14
funcao.perguntaAletoria("Digite seu meio de transporte abaixo :", 26, 27)
#pergunta 15
funcao.perguntaAletoria("Digite sua religião abaixo :", 28, 29)
#pergunta 16
funcao.perguntaAletoria("Digite seu estado social civil abaixo :", 30, 31)
#pergunta 17
funcao.perguntaAletoria("Digite seu videogame favorito abaixo :", 32, 33)
#pergunta 18
funcao.perguntaAletoria("Digite seu lanche favorito abaixo :", 34, 35)
#pergunta 19
funcao.perguntaAletoria("Digite qual festa gosta de ir civil abaixo :", 36, 37)
#pergunta 20
funcao.perguntaAletoria("Digite seu doce favorito abaixo :", 38, 39)
principal.mainloop()