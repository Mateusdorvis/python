class Carro:
    def __init__(self, modelo, marca, cor, usado_ou_nao, local_de_venda ):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.ususado_ou_nao =usado_ou_nao
        self.local_de_venda = local_de_venda

        
      
car = Carro("Honda civic,","Honda", "Preto,", "Usado,", "Porto Alegre, concessionária Via Porto")
print(car.modelo, car.marca, car.cor, car.ususado_ou_nao, car.local_de_venda)



