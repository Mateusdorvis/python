print("qual o maior ?")
x = int(input("insira um número :"))
y = int(input("insira outro :"))
if y>x:
    print(f"{y} é maior do que {x}")
elif x==y:
    print("iguais")
else:
    print(f"{x} é maior que {y}")