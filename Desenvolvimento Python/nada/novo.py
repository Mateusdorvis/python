class Pessoa:
    def __init__(self,nome , idade):
        self.nome = nome
        self.idade = idade
    def __repr__(self):
        return f"Pessoa(nome'{self.nome}), idade={self.idade}"

lista_pessoa=[]
nomes = ["Alice", "Mário", "João"]
idades = [12, 15, 18]

for nome, idade in zip(nomes,idades) :
          lista_pessoa.append(Pessoa(nome,idade))

print(lista_pessoa)