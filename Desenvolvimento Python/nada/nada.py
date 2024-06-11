from datetime import datetime

class Pagamento:
    def __init__(self):
        self.vencimento = datetime(2024, 6, 30)

class PagamentoBoleto(Pagamento): #classe herdeira da classe pai (pagamento)
    def __init__(self, codigo_barras: str):
        self.codigo_barras = codigo_barras

# Exemplo de uso da classe PagamentoBoleto
vencimento = datetime(2024, 6, 30)
codigo_barras = "12345678901234567890"

pagamento_boleto = PagamentoBoleto(codigo_barras)

print("Vencimento: {}.".format(vencimento))
print("Código de Barras: {}".format(pagamento_boleto))


