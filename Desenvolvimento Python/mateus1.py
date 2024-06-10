#desafio 1 da aula 12.04
number1 = int(input("Um número :"))
number2 = int(input("Um número :"))
if number1 > number2: #se o primeiro número for maior 
    print("o  primeiro número é maior pois é {}".format(number1))
elif number1 == number2:
    print(" ambos são iguais")
else: # se o primeiro não for maior 
     print("o segundo número pois é {}".format(number2))
