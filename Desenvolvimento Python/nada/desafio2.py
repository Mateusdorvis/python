class Peixe:
    def __init__(self,especie, agua, profundidade):
        self.especie = especie
        self.agua = agua
        self.profundidade =profundidade
    def __repr__(self):
        return f"Peixe(nome{self.especie}), Tipo : {self.agua}, Profundidade : {self.profundidade}"


peixe1 = Peixe("Peixe-boi", "água-doce", 3)
peixe2 = Peixe("Peixe-espada", "água-doce", 3)
peixe3 = Peixe("Tubarão", "água-salgada", 3)
peixe4 = Peixe("Tubarão-brnaco", "água-salgada", 3)
peixe5 = Peixe("Baleia-azul", "água-salgada", 3)

lista_peixe=[peixe1, peixe2, peixe3, peixe4, peixe5]

for peixe in lista_peixe:
    print(f"Nome do peixe: {peixe.especie},  Habitat : {peixe.agua}, profundidade: {peixe.profundidade}")
