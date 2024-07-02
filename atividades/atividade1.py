import tkinter as tk
from tkinter import ttk

principal = tk.Tk()
principal.title("Labels")

label1 = tk.Label(principal, text="label 1", font=("Arial", 12), fg="white", background="red")
label1.pack(side="right")

label2 = tk.Label(principal, text="label 2", font=("Arial", 12), fg="white", background="blue")
label2.pack(side="right")

label3 = tk.Label(principal, text="label 3", font=("Arial", 12), fg="white", background="green")
label3.pack(side="right")

principal.mainloop()