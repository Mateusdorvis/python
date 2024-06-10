valor_depositado = 0
valor_depositado += float(input(f"Digite um valor 0.70% a.m"))

def calculo(v):
   v *= 0.0070
   return v
valor = calculo(valor_depositado)
valor_depositado +=valor
print("Depois de 1 mes o seu valor {} rendeu".format(valor_depositado))


     