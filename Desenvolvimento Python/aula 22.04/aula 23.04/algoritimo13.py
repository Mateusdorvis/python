gasto = 0

pergunta_beber = int(input("Você deseja beber ? digite [1] sim e [2] não. "))
if not pergunta_beber==1 and not pergunta_beber==2:
    print("opção inválida")
pergunta_comida = int(input("Você deseja comer algo ? digite [1] sim e [2] não. "))
if not pergunta_comida==1 and not pergunta_comida==2:
    print("opção inválida")
pergunta_transporte = int(input("Você deseja pegar transporte ? digite [1] sim e [2] não. "))
if not pergunta_transporte==1 and not pergunta_transporte==2:
    print("opção inválida")

pergunta_amigos = int(input("Vai quantas pessoas com você ?  "))

def calc_gasto(x, y,z, a):
    global gasto
    if x==1:
        gasto+=80
    if y==1:
        gasto+=60
    if z==1:
        gasto+=15
    if a> 0:
        gasto+=gasto *a+1
calc_gasto(pergunta_beber, pergunta_comida, pergunta_transporte, pergunta_amigos)

print(f"o gasto estimado é {gasto}")



    
          
