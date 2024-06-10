escolha_caso = int(input("Calculadora, o que você vai querer calcular ? Digite [1] se quer saber a média entre os números, digite [2] se quer saber a diferença entre os números, digite [3] se quer saber o produto sobre os números , digite [4] se quer saber a divisão :"))

def escolha_user(escolher):
    
    match escolher:
        case escolher if  escolher==1:
            print("Você queres saber a média correto ? ")
           
            def media():
                um = float(input("Digite um número :"))
                dois = float(input("Digite um número :"))
                media_entre = (um + dois) /2
                print(f"A média entre {um} e {dois} é igual a {media_entre}, pois ( {um} + {dois} ) / 2 = {media_entre}")
                return
            media()

        case escolher if escolher==2:
            print("Você queres saber a diferença  entre os números correto ?")

            def subtracao():
                tres = float(input("Digite um número :"))
                quatro = float(input("Digite um número :"))
                sub = tres - quatro 
                print(f"A diferença entre {tres} e {quatro} é igual a {sub}, pois {tres} - {quatro} = {sub}")
                return
            subtracao()

        case escolher if escolher==3:
            print("Você queres saber o produto entre os números correto ?")

            def produto():
                cinco = float(input("Digite um número :"))
                seis = float(input("Digite um número :"))
                prod = cinco * seis 
                print(f"O produto entre {cinco} e {seis} é igual a {prod}, pois {cinco} x {seis} = {prod}")
                return
            produto()

        case escolher if escolher==4:
             print("Você queres saber o produto entre os números correto ?")

             def divisao():
                sete = float(input("Digite um número :"))
                oito = float(input("Digite um número :"))
                div = sete / oito 
                print(f"A divisão entre {sete} e {oito} é igual a {div}, pois {sete} / {oito} = {div}")
                return
             divisao()
        case _:
            print("Desculpa - me, não conseguir identificar qual opção queres :/ .")
escolha_user(escolha_caso)
            
        
        
            
        
    