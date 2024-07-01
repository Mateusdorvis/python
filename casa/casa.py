class Casa:
    def __init__(self, cor_da_casa_externo, numero_da_casa, endereco, proprietario, numer_janelas, n_porta):
        self.cor_da_casa_externo = cor_da_casa_externo
        self.numero_da_casa = numero_da_casa
        self.endereco = endereco
        self.propreitario = proprietario
        self.numer_janelas = numer_janelas
        self.porta = n_porta
    
    def information(self):
       informacao = f"Cor da casa : {self.cor_da_casa_externo}, Numero da casa : {self.numero_da_casa}, Endereço : {self.endereco}, Proprietário da casa : {self.propreitario}, Numero de janelas : {self.numer_janelas}, numero de portas : {self.porta}"
       for i in informacao:
           print(i)
        