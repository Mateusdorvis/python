class Shark:
    def nadar(self): 
        print("Ele está nadando, cuidado !")
    def nadar_de_costas(self):
        print("O tubarão não nada para trás")
    def esqueleto(self):
        print("O esqueleto do tubarão é cartilagem")

class Clowfish:
    def nadar(self):
        print("o peixe palhaço está nadando")
    def nadar_de_costas(self):
        print("O peixe não nada para trás")
    def esqueleto(self):
        print("O esqueleto do peixe é osso")

shark = Shark()
shark.esqueleto()

clowfish = Clowfish()
clowfish.esqueleto()
