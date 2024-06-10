y = int(input("Digite o quantas  laranjas que queira tirar de Pedro. O menino tirou 10 laranjas suco na casa da tia dele:  "))
porc = (100*y)/ 10
if  porc > 50.0 :
  print(" Pedro não ficou feliz por ter tirado {} % laranjas, pois ficou somente com {} %. :/ ".format(porc, y))
elif  50.0 == porc :
  print(" Pedro  ficou meio bravo por ter tirado a metade que tirou. :| ".format(porc))
else:
    print(" Pedro ficou feliz por ter tirado {} %, pois ele ficou {} %. :)".format(porc, y)) 
