import os
import time
import pygame
import pygame_gui

pygame.init()

White = (225,225,225)
Black = (0,0,0)
Red = (225,0,0)
Clock = pygame.time.Clock()
Display_Width = 1200
Display_Height = 600
Gui_Display = pygame.display.set_mode((Display_Width, Display_Height))
Large_Text = pygame.font.Font('freesansbold.ttf', 15)
pygame.display.set_caption('Service Ticket Demo')

def text_objects(text, font):
    TextSurface = font.render(text, True, Black)
    return TextSurface, TextSurface.get_rect()

#def Show_Position():
#    Gui_Exit = False
#    while not Gui_Exit:
#        for event in pygame.event.get():
#            if event.type == pygame.QUIT:
#                Gui_Exit = True
               
#        Gui_Display.fill(White)
#        pygame.display.update()
#        Clock.tick(60)
#    pygame.quit()

def Start_Menu():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        Gui_Display.fill(White)
        print (event) 
        TextSurf, TextRect = text_objects("Please add data entry and instructions, funtionalities, etc", Large_Text)
        TextRect.center = ((Display_Width/2), (Display_Height/2))
        Gui_Display.blit(TextSurf,TextRect)
        pygame.display.update()
        Clock.tick(60)
    pygame.display.update()
    Clock.tick(60)    


#raw_input = input ('Press Enter to exit')
Start_Menu()
Show_Position()
time.sleep(4)


quit()