import tkinter as tkt
from tkinter import ttk

window = tkt.Tk()
window.title("Mudando as cores")

texto = tkt.Label(window,text='Texto Aleatorio',font=("Arial sans", 15))
texto.pack()


#alterando a cor para vermelho
btn1 = tkt.Button(window, text="alterar a janela o plano de fundo  paravermelho", command=lambda : window.config(background="#c21a01")) #lambada susbtiui a função que queria criar (def alterar_cor), na qual renderia linhas de códigos
btn1.pack(side="top")

#alternado a cor de fundo para amarelo
btn2 = tkt.Button(window, text="alterar a janela o plano de fundo para amarelo", command=lambda : window.config(background="#fcaf14"))
btn2.pack(side="top")

#alternado a cor de fundo para azul
btn3 = tkt.Button(window, text="alterar a janela o plano de fundo  paraazul", command=lambda : window.config(background="#066699"))
btn3.pack(side="top")

#alternado a cor de fundo para laranja
btn4 = tkt.Button(window, text="alterar a janela o plano de fundo  paralaranja", command=lambda : window.config(background="#e4491c"))
btn4.pack(side="top")

#alternado a cor de fundo para verde
btn5 = tkt.Button(window, text="alterar a janela o plano de fundo para verde", command=lambda : window.config(background="#aedd2b"))
btn5.pack(side="top")

#alternado a cor de fundo para marrom
btn5 = tkt.Button(window, text="alterar a janela o plano de fundo para marrom", command=lambda : window.config(background="#a04b26"))
btn5.pack(side="top")

#alternado a cor de fundo para padrão
btn6 = tkt.Button(window, text="alterar a janela o plano de fundo para padrão", command=lambda : window.config(background="white"))
btn6.pack(side="top")

#alternado a cor de fundo para preto
btn7 = tkt.Button(window, text="alterar a janela o plano de fundo para preto", command=lambda : window.config(background="black"))
btn7.pack(side="top")

window.mainloop()

   