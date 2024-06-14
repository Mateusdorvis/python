

def funcao():
     print("Vamos fazer a operação")  
     x = int(input("digite 1 para multiplicação, 2 para divisão, 3 para subtração, 4 para adição:  "))
     if x==1:

        print("ok, vamos fazer a multiplicação")
         #função multiplicação
        def mult():
           
           num1= float(input("um número:"))
           num2= float(input("um número:"))
           val = num1*num2
           print()
           return f"{num1} x {num2}  = {val}"
        mult()
     elif x==2:

        print("ok, vamos fazer a divisão")
        def div():
            #função divisão
           num3= float(input("um número:"))
           num4= float(input("um número:"))
           var = num3/num4
           return f"{num3} / {num4}  = {var}"
        div()

     elif x==3:

        print("ok, vamos fazer a subtraçao")
        #função e subtração
        def sub():
           num5= float(input("um número:"))
           num6= float(input("um número:"))
           value = num5-num6
           return f"{num5} - {num6}  = {value}"
        sub()
     elif x==4:

        print("ok, vamos fazer a adição")
        #função adição se caso o user digitar 4
        def adi():
           num7= float(input("um número:"))
           num8= float(input("um número:"))
           valor = num7+num8
           return f"{num7} + {num8}  = {valor}"
        adi()

     if x!=1 and x!=2 and x!= 3 and x!= 4 :
         print("inválido")
funcao()
     
