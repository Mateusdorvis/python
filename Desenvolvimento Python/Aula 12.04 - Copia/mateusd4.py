#nota do aluno
print("Notas de 0 a 10")

nota = float(input("digite sua nota :"))

if (nota < 6.0): # se a nota for menor do que 6.0 é tal nota
    print("Nota F")
elif nota>6.0 and nota <=7.0 :# se a nota for maior igual a 6.0 menor igual a 7 será tal nota. #and limita os valores.
    print("Nota D")
elif nota >7.0 and nota <=8.0 :#se a nota for igual a 9.0 e ou maior mas for menor que 10.0 é tal nota.
    print("Nota C")
elif nota >8.0 and nota <=9.0 :#se a nota for igual a 9.0 e ou maior mas for menor que 10.0 é tal nota.
    print("Nota B")
elif nota >9.0 and nota <=10.0 : #se a nota for igual a 9.0 e ou maior mas for menor que 10.0 é tal nota 
    print("Nota A")   #dica impórtante pode repetir elif várias vezes
else:
    print("Você digitou errado os valores")
   
    
