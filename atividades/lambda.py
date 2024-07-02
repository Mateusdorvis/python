def times(n):
    return lambda x: x * n

double = times(2) #Chamado 1: Aqui está passando o valor de n
result = double(4)#Chamado 2: Aqui está passando valor de x
print(result)


