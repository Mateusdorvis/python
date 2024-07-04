import tkinter as tk

# Configuração da janela principal
janela = tk.Tk()
janela.geometry("400x400")
janela.title("Place Layout Example")

# Adicionando labels com posicionamento absoluto
label1 = tk.Label(janela, text="Label 1", bg="red", fg="white")
label1.place(x=10, y=10)


# Executar a aplicação
janela.mainloop()

