#exercicio 3 15.04
a = int(input(" um número inteiro"))
b = int(input(" um número inteiro"))
c = int(input(" um número inteiro"))
if   c > a and c>b and b>a: #se c for maior que a e b, e b maior que a será, a = 1 b = 2 c = 3, 3>2 2>1 , logo 3,2,1
    print(" a ordem é {}, {}, {}".format(c, b, a)) 
elif  a>b and a>c and b<c:#se a for maior que b e c e b maior que c, ex a = 7 b = 6 c = 3, 7>6 6>5, logo 7,6,5
     print(" a ordem será {}, {}, {}".format(a, b, c))
elif  b>c and b>a and a<c:#se a for maior que b e c e a menor que c
     print(" a ordem será {}, {}, {}".format(b, c, a))
elif  a>c and a>b and c>b:
     print(" a ordem será {}, {}, {}".format(a, c, b))
elif  c>a and c>b and a>b: #12, 8, 22 22,12,8
     print(" a ordem será {}, {}, {}".format(c, a, b))
elif  c==a and a>b: #se c e a forem iguais e a (a e c são iguais levando em consideração) maior que b, ex a e c = 8 e b = 4, 8>4 logo 8,8,4
     print(" a ordem será {}, {}, {}".format(c, a, b))
elif  b==a and b>c : #se b e a forem iguais e a (a e c são iguais levando em consideração) maior que c, ex a e b = 8 e c = 4, 8>4 logo 8,8,4
     print(" a ordem será {}, {}, {}".format(a, b, c))
elif  c==a and b==a: #se a b,a e c forem iguais, a, b e c = 4, logo 4, 4, 4
     print(" a ordem será {}, {}, {}".format(a,b ,c))
elif  c==a and b>a and b>c : #se c e a forem iguais e a (a e c são iguais levando em consideração) menor que b, ex a e c = 8 e b = 9, 8<9 logo 9,8,8
     print(" a ordem será {}, {}, {}".format(b, c, a))
elif  b==a and c>a and c>b : #se b e a forem iguais e a (a e c são iguais levando em consideração) menor que c, ex a e b = 8 e b = 9, 8<9 logo 9,8,8
     print(" a ordem será {}, {}, {}".format(c, b, a))
elif  b==c and a>b and a>c : #se c e b forem iguais e b (a e c são iguais levando em consideração) menor que a, ex b e c = 8 e a = 9, 8<9 logo 9,8,8
     print(" a ordem será {}, {}, {}".format(a, b, c))
else:
     print("VocÊ digitou uma letra")
