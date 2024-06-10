dolar = float(input("Digite um valor em doláres $ , do qual você tem :"))
cotacao = float(input("Qual a cotação do real hoje ? Pois a tem dias que o real cai, enquanto nos outros sobre :"))
troca_ponto = str(dolar).replace(".", ",")

def conversao():
    if dolar>=1.1:
           print("A conversão de $",troca_ponto," dolares para reais, é de R$ %.2f" %(dolar*cotacao), " reais.")
    else:
        print("A conversão de $",troca_ponto," dólar para real, é de R$ %.2f" %(dolar*cotacao), " reais")
b = str(conversao).replace(".", ",")
conversao()