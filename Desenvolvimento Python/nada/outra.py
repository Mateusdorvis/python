#fazer classe pai 

class Animal:
    def __init__(self, nome: str, idade: str, tipo: str) :
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
        
class Peixe(Animal):
    def __init__(self, nome: str, idade: str, habitat: str):
        super().__init__(nome, idade=idade,tipo="Tubarão")
        self.habitat = habitat

peixe = Peixe(nome="Tubarão-martelo", idade=5, habitat="Mar e oceanos")
print(f"Nome do peixe: {peixe.nome},tipo : {peixe.tipo}, idade : {peixe.idade}, habitat : {peixe.habitat}.  ")


