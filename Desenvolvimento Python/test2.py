print("Digite a sua idade para saber se é obrigado a votar ou não")
y = int(input("Quantos anos você tem?")) # saída de mensagem para o usuário perguntando a idade
if y >= 18 and y <= 65: #se o usuário digitar um número maior que ou igual a 18 e menor que 65 anos, vai aparcer a seguinte mensagem "você é obrigado" 
    print(" você é obrigado a votar, pois tem {} anos ".format(y))
else: # se não for maior que ou igual e menor ou igual a 65 anos, vai aparcer a mensagem " você não é obrigado"
    print("você não é obrigado a votar, pois tem {} anos ".format(y))

print("Digite os valores se você se inclui nestes requisitos abaixo:")
print("1. Gestante")
print("2. Cadeirante")
print("3. Pessoa com deficiência")
print("4. Idoso")
print("5. Gestante")
print("6. Nenhum")
w = int(input("Digite os número :"))  # saída de mensagem para o usuário perguntando em qual número que se inclui.
if (w==1) or (w==2) or (w==3) or (w==4) or (w==5): # Se w (variavel criada por  mim, para número que o usuário for digitar) for igual a 1, ou 2, ou, 3, ou 4 , ou 5 o usuario imprime tal mensagem na tela
        print("Você tem prioridade é {}".format(w))
else:
      print("Você não tem prioridade, porque é {}".format(w))
