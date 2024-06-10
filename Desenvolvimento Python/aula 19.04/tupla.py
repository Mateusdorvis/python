#tupla

tupla_numeros = (1, 2, 3, 4, 5 , 6)
soma = sum(tupla_numeros)
produto = 1
for x in tupla_numeros:
    produto *= x
print(" a soma é {}".format(soma))
print(" o produto é {}".format(produto))
