numero = 1
max = int(input("digite um numero inteiro maior que 1 :"))
print("os números pares de {} é".format(max))
while numero<=max:
 if numero%2==1:
        print(numero, end="")
        numero+=2
