
#O que é modulo? modulo no python é criar funções, VARIAVÉIS E CLASSES (OU SEJA TUDO) para serem importadas em outros arquivos, é claro que isso reduz o tempo de desenvolver uma aplicação python, além de  ajudar em milhares de coisas.
#aqui em baixo criamos uma função para ser importada no outro arquivo
def world():
    print("Hello world")

#FAZENDO VARÍAVEL PARA SER IMPORTADA.
texto_aletorio = "Nada por aqui, vai te embora."

class Pessoa():
      def __init__(self, nome, idade, profissao, genero,cidade) :
           self.nome = nome
           self.idade = idade
           self.profissao = profissao
           self.genero = genero
           self.cidade =cidade 
      def msg(self):
           print(f"Seu nome é : {self.nome}, tem : {self.idade} anos, sua profissão é : {self.profissao} e seu gênero é : {self.genero}, mora em :{self.cidade}")
pessoa = Pessoa('Mateus',18, "Desempregado", "Masculino", "Porto Alegre")      
