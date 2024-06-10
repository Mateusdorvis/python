palavras = [] #var vazia, pois o usuário vai digitar alguma coisa e vai direto nesta var.
def adiciona_palavra():
    print("Você deseja adicionar uma palavra?\n Digite qualquer coisa,\n Caso não digitar nada,\n o programa para.")
    entrada = input("digite: ") #se não digitar nada, o programa apaga, mas se digitar alguma coisa, a recursividade vai ser infinita
    if entrada == "": #se a entrada for vazia, o programa acaba
        print("você não digitou nada, fim do programa.")
        print(palavras)
    else: # se não estiver vazia
        palavras.append(entrada)
        adiciona_palavra()

adiciona_palavra()
