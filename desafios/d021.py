import pygame

#simple music player
desafio = 'desafio 21'
print(f'{desafio:=^50}')

pygame.init()
pygame.mixer.music.load('desafios/d021.mp3')
pygame.mixer.music.play()
input('Pressione ENTER para parar...')
pygame.event.wait()