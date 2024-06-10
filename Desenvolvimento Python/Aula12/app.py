
escreva = str(input("Digite qualquer caractere :"))
arquivo_txt = open("aula12/text3.txt","w")
print(arquivo_txt)
while True:
  if escreva==" ":
              arquivo_txt = open("aula12/text3.txt","a")
              arquivo_txt.write(escreva)
              arquivo_txt.close()
              print(f"{escreva}")
 
  else:
        print("programa acabou\n")  
        print(arquivo_txt.read())
        arquivo_txt.close()

 
          

