nova_frase = []
def adiciona_frase():
    print("Você deseja adicionar uma palavra?\n Digite qualquer coisa,\n Caso não digitar nada,\n o programa para.")
    escreva_algo = input("digite: ")
    if escreva_algo == "":
        print("você não digitou nada, fim do programa.")
        print(nova_frase)
    else:
        nova_frase.append(escreva_algo)
        adiciona_frase()

adiciona_frase()