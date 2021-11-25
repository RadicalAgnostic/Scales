"""

Welcome to the scale series!!!

This version uses the reset function to reset the strings

"""


import pygame 
import numpy as np
import random
from math import *

pygame.init()
pygame.mixer.init()


"""

These are the functions used in the program

colorChange fills the background with a color and can be used as a reset
playSound uses the stolen code to play a sin wave
drawCircle draws a circle with a border parameter

"""

def drawCircle(color, position, radius, border_size, border_color, ring):
    
    if border_size != 0:
        
        pygame.draw.circle(window, border_color, position, radius + border_size)
        
    pygame.draw.circle(window, color, position, radius, ring)
    pygame.display.update()

def showTime():
    
    pygame.draw.rect(window, (255,255,255), (0,0,300,50))
    time = pygame.time.get_ticks() / 1000
    message = "Time in seconds: {}".format(time)
    window.blit(font.render(message, True, text_color), (10,10))

    message = "Mouse x: " + str(mousex) +  " Mouse y:" + str(mousey)
    window.blit(font.render(message, True, text_color), (10, 30))
        
    pygame.display.update()



"""

Here are the variables for initialization


"""


### Random stuff ###

purple = (100, 0, 160)  
cyan = (0, 240, 255)  
black = (0,0,0)
white = (255,255,255)



### Creates window ###

window_size = (1000,700)
window = pygame.display.set_mode((window_size), pygame.RESIZABLE)
pygame.display.set_caption("Funky Scale Time")

font = pygame.font.SysFont("Sans", 20)
text_color = (black)

window.fill(white)
pygame.display.flip()




### Variables to keep the loop going ###

running = True
play_Loop1 = False
play_Loop2 = False
keylist1 = "1234567890"
keylist2 = "qwertyuiop"


fret_length = (window_size[0] - 200) /12
string_distance = 20    


def reset():
    
    window.fill(white)
    
    for i in range(0,6):
        pygame.draw.line(window, black, (100, 100 + i*string_distance), (window_size[0]-100, 100 + i*string_distance), 2)
    
    for i in range(0,13):
        pygame.draw.line(window, black, (100 + i*fret_length, 100), (100 + i*fret_length, 200), 2)
        
        
    open_notes = "EADGBE"
    i = 0 
    for char in open_notes:
        
        window.blit(font.render(char, True, black), (75, 93 + 20*i))
        i += 1
        
    pygame.display.update()


def fret(string, fret):

    position = (101 + fret*fret_length, 101 + string*string_distance)

    drawCircle(white, position, 5, 2, black, 5)


reset()







while running:
    
    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            
            running = False
            pygame.quit()
            
            
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:

            colorChange(black)
        
        
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_1 and play_Loop1 == False:
            play_Loop1 = True
         
            
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_2 and play_Loop2 == False:
            play_Loop2 = True

            
            
            
            

    if play_Loop1 == True:
            
            
        for i in range (0,13):

            fret(0, i)
        
        
        play_Loop1 = False
    



    if play_Loop2 == True:
        
        
        reset()
        
        
        
        
        play_Loop2 = False


        












































































































































































































