def executar():
   print("Vamos fazer a operação")  

def funcao():
     x = int(input("digite 1 para multiplicação, 2 para divisão, 3 para subtração, 4 para adição:  "))
     if x==1:
        print("ok, vamos fazer a multiplicação")
         #multiplicação
        def mult():
           num1= float(input("um número:"))
           num2= float(input("um número:"))
           val = num1*num2
           print(f"{num1} x {num2}  = {val}")
        mult()
     elif x==2:
        print("ok, vamos fazer a divisão")
        def div():
            #divisão
           num3= float(input("um número:"))
           num4= float(input("um número:"))
           var = num3/num4
           print(f"{num3} / {num4}  = {var}")
        div()
     elif x==3:
        print("ok, vamos fazer a subtraçao")
        #subtração
        def sub():
           num5= float(input("um número:"))
           num6= float(input("um número:"))
           value = num5-num6
           print(f"{num5} - {num6}  = {value}")
        sub()
     elif x==4:
        print("ok, vamos fazer a adição")
        #adição se caso o user digitar 4
        def adi():
           num7= float(input("um número:"))
           num8= float(input("um número:"))
           valor = num7+num8
           print(f"{num7} + {num8}  = {valor}")
        adi()
     elif x==" ":
        print("digite um número")
     else:
         print("inválido")
funcao()
     
