Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nome = input("digite seu nome, por gentileza :")
digite seu nome, por gentileza : mateus
>>> print ("seja bem vindo {} ! ".format(nome))
seja bem vindo  mateus ! 
>>> idade = int(input("digite sua idade :"))
digite sua idade : 18
>>> peso = float(input("digite seu peso :"))
digite seu peso : 78.6
>>> troca = str(peso).replace(".",",")
>>> print("Suas informações estão salvas, seu nome é {}, sua idade é {} e você pesa {} ? Correto? ".format(nome, idade, troca))
Suas informações estão salvas, seu nome é  mateus, sua idade é 18 e você pesa 78,6 ? Correto? 
>>> Suas informações estão salvas, seu nome é  mateus, sua idade é 18 e você pesa 78,6 ? Correto?
SyntaxError: invalid syntax
>>> SyntaxError: invalid syntax
SyntaxError: invalid syntax
