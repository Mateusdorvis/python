port = float(input("Digite a nota de Português "))
ing = float(input("Digite a nota de ingês "))

media = (port + ing) / 2

if media >= 7.0 and  media<=7.9 :
     print(" está na média")
elif media >= 8.0 and media<= 10.0:
     print(" está na aprovado")
else:
    print("reprovado")


