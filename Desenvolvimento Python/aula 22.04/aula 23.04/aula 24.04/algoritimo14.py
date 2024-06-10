sexo_user = int(input("Qual seu sexo ? digite [1] para sexo masculino, ora [2] para sexo feminino :"))

if sexo_user==1:
 print("Você digitou 1")
 def pergunta_masc():
    data_user = int(input("qual ano você começou a trabalhar ? digite [0] se não souber ou [1] se souber :"))
    if data_user==0:
          def  pergunta_3():
            idade = int("Com quantos anos vc contribuiu com a previdência?")
            valor = 65-idade
            print(f" Terá mais {valor} anos de trabalho.")
            return idade,valor
    pergunta_3()
    if data_user==1:
     def  pergunta_2():
            #funçao para perguntar que ano que trabalhou se o user respondeu
            n =  int(input("qual atual ? :"))
            b = int(input("qual ano que você começou a trabalhar ? :"))
            m = n - b
            sub = 65 - m
            print(f"Você tem {m} anos de trabalho e terá que trabalhar por mais {sub}")
            return n,b,m,sub
    pergunta_2()  
    return data_user
pergunta_masc()

if sexo_user==2:
  print("Voce digitou 2")
  def fem():
     #funçao para pergunta do caso fem
     data = int(input("qual ano você começou a trabalhar ? digite [0] se não souber ou [1] se souber :"))
     if data==0:
        print("ok, vamos para outra etapa")
     else: 
        def  pergunta_2():
            #funçao para perguntar que ano que trabalhou se o user respondeu
            um =  int(input("qual atual ? :"))
            dois= int(input("qual ano que você começou a trabalhar ? :"))
            tres = um - dois
            quatro =  62 - tres
            print(f"Você tem {tres} anos de trabalho e terá mais {quatro} anos de trabalho.")
            return um,dois,tres,quatro
        pergunta_2()

     ano = int("Com quantos anos vc contribuiu com a previdência?")
     calculo = 62-ano
     print(f" Terá mais {calculo} anos de trabalho.")
     return ano,data,calculo
  fem()
else: 
 print("invalido")

