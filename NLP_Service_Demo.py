import os
import time
import tensorflow
import nltk
import pygame
import pygame_gui

pygame.init()

 pygame.display.set_caption('Quick Start')
 window_surface = pygame.display.set_mode((800, 600))

 background = pygame.Surface((800, 600))
 background.fill(pygame.Color('#000000'))

 is_running = True

 while is_running:

     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             is_running = False

     window_surface.blit(background, (0, 0))

     pygame.display.update()


print ("hello")

Service_Ticket = input ("Enter Ticket:")

VPN_Arr = ["vpn", "VPN"]
Adobe_Arr = ["Adobe", "adobe", "ADOBE", "PDF", "pdf"]

if any(c in Service_Ticket for c in VPN_Arr):
    print ("contains vpn")
elif any(c in Service_Ticket for c in Adobe_Arr):
    print ("contains adobe")
else:
    print ("does not contain key words: vpn or adobe")
 
raw_input = input ('Press Enter to exit')
