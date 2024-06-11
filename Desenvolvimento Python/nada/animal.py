class Animal: #classe mãe 
    def __init__(self, nome: str, tipo: str, idade: int, cor_do_pelo: str, raca: str):
        self.nome = nome  #objeto 1
        self.tipo = tipo  #objeto 2
        self.idade = idade  #objeto 3
        self.cor_do_pelo = cor_do_pelo  #objeto 4
        self.raca = raca   #objeto 5

class Cachorro(Animal):#esta classe é herdeira (classe filha)da outra, logo é subclasse
    def __init__(self, nome: str, idade: int, cor_do_pelo: str, raca: str, som: str):
        super().__init__(nome, tipo="Cachorro", idade=idade, cor_do_pelo=cor_do_pelo, raca=raca) #init da classe cachorro(herdeira da animal) e super () serve para classe herdeira (classe filha e subclasse), a primeira init é da classe mãe e a 2segunda init é da classe filha
        self.som = som

# Exemplo de uso da classe Animal e Cachorro
animal = Animal(nome="Rex", tipo="Cachorro", idade=5, cor_do_pelo="Marrom", raca="Labrador")
print(f"Animal: {animal.nome}, Tipo: {animal.tipo}, Idade: {animal.idade}, Cor do Pelo: {animal.cor_do_pelo}, Raça: {animal.raca}")

cachorro = Cachorro(nome="Bobby", idade=3, cor_do_pelo="Preto", raca="Poodle", som="Au Au")
print(f"Cachorro: {cachorro.nome}, Tipo: {cachorro.tipo}, Idade: {cachorro.idade}, Cor do Pelo: {cachorro.cor_do_pelo}, Raça: {cachorro.raca}, Som: {cachorro.som}")
