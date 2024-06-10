#exercicio 2
print("multiplicação, adição, subtração e divisão")
x = int(input("digite um número :"))
y = int(input("digite um número :"))

#com parametros a e b
def calculo(a,b):
   print("a operação da multiplicação",a * b)
   print("a operação da adição ",a + b)
   print("a operação da divisão",a / b)
   print("a operação da subtração ",a - b)
calculo(x,y) #as variaveis globais x e y são argumento
#ou pode fazer sem os paremetros, como eu fiz neste exemplo
print("multiplicação, adição, subtração e divisão")
x = int(input("digite um número :"))
y = int(input("digite um número :"))

def calculadora():
   print("a operação da multiplicação",x * y)
   print("a operação da adição ",x + y)
   print("a operação da divisão",x / y)
   print("a operação da subtração ",x - y)
calculadora()
