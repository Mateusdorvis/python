#desafio 3 16.04
import random

numero_aleatorio = random.randint(1,10)
aleatorio = None
conta = 0

while aleatorio != numero_aleatorio:
    aleatorio = int(input("Adivinha o número entre 1 a 10 :"))
    conta += 1
    if aleatorio>4 or aleatorio<4:
      print("Quase lá, tente um número maior ou menor que você digitou")
    elif  aleatorio==4:
        print("Acertou")
        conta+=0
    else:
       print("suas tentativas foram",conta)
 

