from tkinter import Tk, Text

root = Tk()
root.resizable(True, True)
root.title("Text Widget Example")

text = Text(root, height=8)
text.pack()

text.insert('1.0', 'This is a Text widget demo\n')
text.insert('1.5', 'ojojojojojojojo')#T(Caractere 1)H(Caractere 2)I(Caractere 3)S(Caractere 4) ojojojojojojojo(Caractere 5)
root.mainloop()