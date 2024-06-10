y = int(input("Digite um número para saber de tal produto :"))
def digite_int(value):

 match value:
   #match é utilizado para casos, se tal coisa não cai no if, nem else, nem elif vai para case, que é uma alternativa
      case value if value==1:# se caso o usuário digitar um valor igual a 1 é para imprimir 
       print("Aliemnto não - perecível")
      case value if value==2 or value==3 or value==4 :# se caso o usuário digitar 2 ou 3 ou 4 é para imprimir
       print("Aliemnto perecível")
      case value if value==5 or value==6:# se caso o usuário digitar digitar
       print("Vestuário")
      case value if value==7:# se caso o usuário digitar
       print("Higiene pessoal")
      case value if value>=8 and value<=15:# se caso o usuário digitar
       print("Limpeza e utensilios domésticos")
      case _:
       print("Código invalído")
digite_int(y)

        