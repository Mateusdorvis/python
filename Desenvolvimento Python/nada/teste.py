class Pagamento:
    def PodeSerPago(self):
        # Implementação padrão do método PodeSerPago para a classe base Pagamento
        # Você pode definir a lógica padrão aqui ou deixar como um método abstrato
        # que deve ser sobrescrito nas subclasses
        return True

class PagamentoBoleto(Pagamento):
    def PodeSerPago(self):
        # Implementação do método PodeSerPago para a classe PagamentoBoleto
        # Se desejar, você pode chamar o método da classe base usando super() e
        # adicionar funcionalidades adicionais ou substituir completamente o método
        return False  # Exemplo de implementação diferente para PagamentoBoleto

# Exemplo de uso
pagamento = Pagamento()
print(pagamento.PodeSerPago())  # Saída: True

pagamento_boleto = PagamentoBoleto()
print(pagamento_boleto.PodeSerPago())  # Saída: False





