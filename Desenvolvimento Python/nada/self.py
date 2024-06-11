class Pessoa:
    def __init__(self,nome,idade):
      self.nome = nome
      self.idade = idade
      

    def verificar_nome(self):
        print(f"seu nome é {self.nome}")

    def verifica_idade(self):
        if self.idade >= 18:
            print(" Você é é maior de idade.")
        else:
            print("VocÊ é menor de idade.")

  

pessoa1 = Pessoa("Ana", 19)
pessoa1.verificar_nome()
pessoa1.verifica_idade()

        
        




