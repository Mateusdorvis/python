# conversão C para F (fisíca)
a = float(input("Digite uma temperatura em Graus Celsius (C)"))
celsius = str(a).replace(".", ",")

def farhent(c):
    return (9*c+160) / 5
temperature = farhent(a)
v = str(temperature).replace(".", ",")
print("A temperatura de {} °C é igual a {} °F ".format(celsius, v))