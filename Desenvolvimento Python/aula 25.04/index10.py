print("Digite 10 números inteiros...")

um = int(input("Digite um número inteiro"))
dois = int(input(" Digite um número inteiro :"))
tres = int(input(" Digite um número inteiro :"))
quatro = int(input(" Digite um número inteiro :"))
cinco = int(input(" Digite um número inteiro :"))
seis = int(input(" Digite um número inteiro :"))
sete = int(input(" Digite um número inteiro :"))
oito = int(input(" Digite um número inteiro :"))
nove = int(input(" Digite um número inteiro :"))
dez =int(input(" Digite um número inteiro :"))

lista = [um, dois, tres, quatro, cinco, seis, sete, oito, nove, dez]

if um<=0 or dois<=0 or tres<=0 or quatro<=0 or cinco<=0 or seis<=0 or sete<=0 or oito<=0 or nove<=0 or dez:
    def revers():
      global lista
      lista.reverse()
      print(lista)
    revers()
else: 
   print(lista)

    

