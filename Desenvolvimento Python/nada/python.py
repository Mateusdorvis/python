class Aluno:
    #esta função init é importante porque vamos chamar na atribuição
    def __init__(self, idade):
        self.idade = idade
    #def -init_() é uma função específica para classe
  #instancia é quando chamo

    def verifica_idade(self):
        if self.idade >= 18:
            print("O aluno é maior de idade.")
        else:
            print("O aluno é menor de idade.")

#se botar self não vai funcionar nada, self inicia 
aluno1 = Aluno(20)
aluno1.verifica_idade()  # Saída: O aluno é maior de idade.

aluno2 = Aluno(16)
aluno2.verifica_idade()  # Saída: O aluno é menor de idade.
