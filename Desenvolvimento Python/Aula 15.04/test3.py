numero = 1
max = int(input("Digite um número inteiro maior que 1:"))

print("Numero pares entre 1 e", max, ":")

while numero <= max:
    if numero%2==0:
         print(numero, end="")
    numero+=1