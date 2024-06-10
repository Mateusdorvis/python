print(" Parcelamento ")
prestacao = int(input(" Digite por qual valor compraste um objeto:"))
div = int(input("Digite quantos meses vai pagar o objeto que comprara:"))
def calculo():
  print("Sua prestação será de R$%.2f" %(prestacao / div))
calculo()