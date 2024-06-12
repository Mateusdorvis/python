class Pessoa:
    def __init__(self,nome , idade):
        self.nome = nome
        self.idade = idade
    def __repr__(self):
        return f"Pessoa(nome'{self.nome}), idade={self.idade}"
    
pessoa1 = Pessoa("Alice",15)
pessoa2 = Pessoa("Otavio",17)
pessoa3 = Pessoa("Pedro",19)

lista_pessoa=[pessoa1,pessoa2, pessoa3]

print(lista_pessoa[2])
