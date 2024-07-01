
class Casa:
    def __init__(self, cor_da_casa_externo, numero_da_casa, endereco, proprietario, numer_janelas, n_porta, n_comodo):
        self.cor_da_casa_externo = cor_da_casa_externo
        self.numero_da_casa = numero_da_casa
        self.endereco = endereco
        self.propreitario = proprietario
        self.numer_janelas = numer_janelas
        self.porta = n_porta
        self.comodo = n_comodo
    def informacao(self):
        dicionario = {"cor": f"{self.cor_da_casa_externo}"}
