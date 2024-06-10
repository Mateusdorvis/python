x = int(input("Digite o número de laranjas que queira tirar de Pedro. O menino tirou 10 laranjas suco na casa da tia dele:"))
sub = 10 - x
if  x > 5:
  print(" Pedro não ficou feliz por teres tirado {} laranjas e ter ficado somente com {} :/ ".format(x, sub)) # se x > do que 5, exemplo digito 6 (10 - 6 = 4), não ficou feliz, logo 6 é maior do que 5
elif  5 == x:
  print(" Pedro  ficou meio bravo por teres tirado a metade que tirou. :| ".format(x)) # se x e 5 forem iguais, exemplo 5 é igual 5
else:
    print(" Pedro ficou feliz por teres tirado {} e ter ficado somente com  {}. :)".format(x, sub)) # se x for menor do que 5, exemplo digito 3 (10 - 3 = 7 ), ficou feliz logo 3 é menor do que 5



