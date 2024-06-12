#condição exercíos 
class Tubarao:
    animal_tipo = "fish"
    location = "oceano"
    flo = 0

    def __init__(self, nome, tipo):
         self.nome = nome
         self.tipo = tipo

    def set_fo(self, flowers):
        self.flo = flowers
        print("Nada " + str(flowers) + "follwers")


sammy = Tubarao("olá", 4)
print(sammy.nome)
print( sammy.location)

stvie = Tubarao("nada", 4)
print(stvie.nome )
stvie.set_fo(77)
print(stvie.animal_tipo)

