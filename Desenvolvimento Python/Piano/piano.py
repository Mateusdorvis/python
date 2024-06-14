import pygame
import time
from pygame.locals import *

# Inicialização do Pygame
pygame.init()

# Definindo as dimensões da janela
largura = 800
altura = 200
tamanho_tecla = 60

# Definindo cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# Criando a janela
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Piano Simples")

# Carregando sons das teclas
sons = {
    K_a: pygame.mixer.Sound("nota1.wav"),
    K_s: pygame.mixer.Sound("nota2.wav"),
    K_d: pygame.mixer.Sound("nota3.wav"),
    K_f: pygame.mixer.Sound("nota4.wav"),
    K_g: pygame.mixer.Sound("nota5.wav"),
    K_h: pygame.mixer.Sound("nota6.wav"),
    K_j: pygame.mixer.Sound("nota7.wav")
}
do = pygame.mixer.Sound("nota1.wav")
re = pygame.mixer.Sound("nota2.wav")
mi = pygame.mixer.Sound("nota3.wav")
fa = pygame.mixer.Sound("nota4.wav")
sol =pygame.mixer.Sound("nota5.wav")
la = pygame.mixer.Sound("nota6.wav")
si = pygame.mixer.Sound("nota7.wav")

def roda_music():
    do.play()
    time.sleep(0.5)
    re.play()
    time.sleep(0.5)
# Loop principal
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            executando = False
        elif evento.type == KEYDOWN:
            if evento.key in sons:
                sons[evento.key].play()

    # Desenhar o piano na tela
    janela.fill(branco)
    for i, (tecla, som) in enumerate(sons.items()):
        pygame.draw.rect(janela, preto if i % 2 == 0 else branco, (i * tamanho_tecla, 0, tamanho_tecla, altura))
    pygame.display.flip()

# Finalizando o Pygame
pygame.quit()
