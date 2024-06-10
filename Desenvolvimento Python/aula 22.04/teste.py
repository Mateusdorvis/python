#argumento e parametro

def add(fname, mateus, dorvis):#paremetros a e b, os parametros pode ser de 2 ou até mais de dois parametros
       print(fname + " " + mateus +" "+ dorvis) #se não colocar "", vai ficar refreshbar, pois " " é espaço
add("grande", "refresh", "bar")#grande e refresh são argumentos, se colocar 2 ou mais de 2, o argumento deve contar quantos parametros eu coloquei, se coloquei 3 parametros, tenho que colocar 3 argumentos, se colocar 2 ou 1, o código vai estar errado

def kid(*kids):#* representa um número desconhecido quantas vezes (x) que chamar aquele parametro
       print("As crianças são " + kids[3])#kids [1] é indíce que adicionei dentro desta função
kid("Chatas", "fofas", " barulhentas")

#soma

