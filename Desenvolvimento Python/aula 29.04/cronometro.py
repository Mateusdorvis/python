#Você obteve um programa no slide anterior que calcula quantos segundos se passaram. Agora faça um programa em contagem regressiva que, dado um determinado minuto (ex : 5 minutos). Mostre a contagem regressiva até chegar em 00:00 para o usuário.



import time

segundos = 0
minutos = 1

#minutos = input("quantos minutos vc deseja esperar ")
#segundos = int("e agora quantos segundos ?")
print(f"{minutos}:{segundos}")
for i in range((minutos*60)+segundos):#1*60 + 0 =60
    time.sleep(.1)#sleep(aqui se altera somente os segundos neste argumento)
  
    if minutos>0:#1 é maior que 0, true
        if segundos>0: #0 é maior que 0 se for true
         segundos-=1
        else: #se for falso, então 1-1, 59
          minutos-=1
          segundos = 59
    elif minutos==0 or segundos>0: #se 1==0 ou 59 maior que 0, 59-1
       segundos-=1
    else:
      print("error 404")
    print(f"{minutos}:{segundos}")

    if minutos==0 and segundos==0:
      print("acabou")
