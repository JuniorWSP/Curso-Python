#Faça um programa que abra e reproduza o áudio de um arquivo MP3.
import pygame  #instala o pygame
pygame.init()  #inicia o pygame
pygame.mixer.music.load('figaro.mp3')  #usa a funcionalidade do mixer e coloca o nome do arquivo
pygame.mixer.music.play()  #inicia o toque da musica
pygame.event.wait()  #encerra o programa quando a musica acabar
