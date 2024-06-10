codigo = int(input("Please, digite o código adquirido :"))

def leia_codigo(code):
    
    match code:
        case code if code==100:
            def cachorro_quente():
                pergunta_1 = int(input(" Vai levar quantos cachorros - quentes ? :"))
                pagamento = pergunta_1 * 1.70
                print(f"Se vai levar {pergunta_1}, então que terá que pagar {pagamento}")
            cachorro_quente()
        case code if code==101:
            def bauru_simples():
                pergunta_2 = int(input(" Vai levar quantos baurus ? :"))
                val = pergunta_2 * 2.30
                print(f"Se vai levar {pergunta_2}, então que terá que pagar {val}")
            bauru_simples()
        case code if code==102:
            def bauru_com_ovo():
                pergunta_3 = int(input(" Vai levar quantos baurus com ovos ? :"))
                valor_a_pagar = pergunta_3 * 2.60
                print(f"Se vai levar {pergunta_3}, então que terá que pagar {valor_a_pagar}")
            bauru_com_ovo()
        case code if code==103:
            def hamburguer():
                pergunta_4 = int(input(" Vai levar quantos hambuergueres ? :"))
                conta = pergunta_4 * 2.40
                print(f"Se vai levar {pergunta_4}, então que terá que pagar {conta}")
            hamburguer()
        case code if code==104:
            def chesburguer():
                pergunta_5 = int(input(" Vai levar cheeseburgueres ? :"))
                value = pergunta_5 * 2.50
                print(f"Se vai levar {pergunta_5}, então que terá que pagar {value}")
            chesburguer()
        case code if code==106:
            def ref():
                pergunta_6 = int(input(" Vai levar quantos refri contigo ? :"))
                valor = pergunta_6 * 2.60
                print(f"Se vai levar {pergunta_6}, então que terá que pagar {valor}")
            ref()
        case _:
            print("Desculpa")

    def levar():
        question = int(input("Vai querer levar mais alguma coisa ? Se sim digite [1] se não digite [2] :"))
        if question==1:
            def levar():
                 digite = int(input("digite um codigo :"))
                 if digite==code:
                     print("Já levou")
                 else:
                     def comprar(d):
                         match d:
                             case d if d==100:
                                 def cao():
                                     c = int(input(" Vai levar quantos cachorros - quentes ? :"))
                                     cal = (c*1.70) + code
                                     return cal,c 
                                 cao()
                             case d if d==101:
                                 def bas():
                                     var1 = int(input(" Vai levar quantos baurus simples? :"))
                                     var2 = (var1*2.30) + code
                                     return var2,var1 
                                 bas()
                             case d if d==102:
                                 def bao():
                                     var3 = int(input(" Vai levar quantos baurus com ovos ? :"))
                                     var4 = (var3*2.30) + code
                                     return var3,var4
                                 bao()
                             case d if d==103:
                                 def ham():
                                     var5 = int(input(" Vai levar quantos baurus com ovos ? :"))
                                     var6 = (var5*2.30) + code
                                     return var5,var6
                                 ham()
                             case d if d==104:
                                 def che():
                                     var7 = int(input(" Vai levar quantos baurus com ovos ? :"))
                                     var8 = (var7*2.30) + code
                                     return var7,var8
                                 che()
                             case d if d==104:
                                 def refrigerente():
                                     var9 = int(input(" Vai levar quantos baurus com ovos ? :"))
                                     var10 = (var9*2.30) + code
                                     return var9,var10
                                 refrigerente()
                             case _:
                                   print("Perdão")
                         comprar()
                 return digite
            levar()

    levar()
  
leia_codigo(codigo)


    
          
        
        