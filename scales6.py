"""
Welcome to the scale series!!!
This version uses the reset function to reset the strings
"""


import pygame as pg
import numpy as np
import random
from math import *

pg.init()
pg.mixer.init()



"""
Things to do:
    
Add neck bar
Move dots to center of frets



"""


"""
These are the functions used in the program
colorChange fills the background with a color and can be used as a reset
playSound uses the stolen code to play a sin wave
drawCircle draws a circle with a border parameter
"""

def drawCircle(color, position, radius, border_size, border_color, ring):
    
    if border_size != 0:
        
        pg.draw.circle(window, border_color, position, radius + border_size)
        
    pg.draw.circle(window, color, position, radius, ring)
    pg.display.update()

def showTime():
    
    pg.draw.rect(window, (255,255,255), (0,0,300,50))
    time = pg.time.get_ticks() / 1000
    message = "Time in seconds: {}".format(time)
    window.blit(font.render(message, True, text_color), (10,10))

    message = "Mouse x: " + str(mousex) +  " Mouse y:" + str(mousey)
    window.blit(font.render(message, True, text_color), (10, 30))
        
    pg.display.update()



"""
Here are the variables for initialization
"""


### Random stuff ###

purple = (100, 0, 160)  
cyan = (0, 240, 255)  
black = (0,0,0)
white = (255,255,255)



### Creates window ###

window_length = 1000
window_height = 700

window_size = (window_length, window_height)
window = pg.display.set_mode((window_size), pg.RESIZABLE)
pg.display.set_caption("Funky Scale Time")

font = pg.font.SysFont("Sans", 20)
text_color = (black)

window.fill(white)
pg.display.flip()



  
distance_from_window_to_frets = 100 * 2 

fret_length = (window_length - distance_from_window_to_frets) /12
string_distance = 20  


def reset():
    
    window.fill(white)
    
    pg.draw.line(window, black, (100, 93), (100,207), 7)
    
    
    for i in range(0,6):
        pg.draw.line(window, black, (100, 100 + i*string_distance), (window_size[0]-100, 100 + i*string_distance), 2)
    
    for i in range(0,13):
        pg.draw.line(window, black, (100 + i*fret_length, 100), (100 + i*fret_length, 200), 2)
        
        
    open_notes = "EBGDAE"
    i = 0 
    for char in open_notes:
        
        window.blit(font.render(char, True, black), (73, 93 + 19*i))
        i += 1
        
    pg.display.update()


def showFret(string, fret):
    
    string -= 1
    
    
    if fret == 0:
        position = (101 + fret*fret_length, 101 + string*string_distance)
    else:
        fret -= 1
        position = (101 + (fret_length * .5) + fret*fret_length, 101 + string*string_distance)

    drawCircle(white, position, 5, 2, black, 5)
    
    pg.display.update()


"""
-------------------
6 = E string
5 = A string
4 = D string
3 = G string
2 = B string
1 = e string
-------------------
"""










E_list  = [[6, 0], [6,12], [5, 7], [4, 2], [3, 9], [2, 5], [1, 0], [1,12]]
Eb_list = [[6,11], [5, 6], [4, 1], [3, 8], [2, 4], [1,11]]
D_list  = [[6,10], [5, 5], [4, 0], [4,12], [3, 7], [2, 3], [1,10]]
Db_list = [[6, 9], [5, 4], [4,11], [3, 6], [2, 2], [1, 9]]
C_list  = [[6, 8], [5, 3], [4,10], [3, 5], [2, 1], [1, 8]]
B_list  = [[6, 7], [5, 2], [4, 9], [3, 4], [2, 0], [2,12], [1, 7]]
Bb_list = [[6, 6], [5, 1], [4, 8], [3, 3], [2,11], [1, 6]]
A_list  = [[6, 5], [5, 0], [5,12], [4, 7], [3, 2], [2,10], [1, 5]]
Ab_list = [[6, 4], [5,11], [4, 6], [3, 1], [2, 9], [1, 4]]
G_list  = [[6, 3], [5,10], [4, 5], [3, 0], [3,12], [2, 8], [1, 3]]
Gb_list = [[6, 2], [5, 9], [4, 4], [3,11], [2, 7], [1, 2]]
F_list  = [[6, 1], [5, 8], [4, 3], [3,10], [2, 6], [1, 1]]


list_of_lists = [E_list, Eb_list, D_list, Db_list, C_list, B_list,  
                 Bb_list, A_list, Ab_list, G_list, Gb_list, F_list]







### Variables to keep the loop going ###

running = True
window_maximized = False

reset()  # prints fretboard the first time


while running:
    
    for event in pg.event.get():


        if event.type == pg.QUIT:
            
            running = False
            
        if event.type == pg.VIDEORESIZE:
            
            # print("the green button was pressed")
            2 + 2
           
            
        elif event.type == pg.KEYDOWN:
            
    
            
            
            if event.key == pg.K_1:
                
                for i in range(0,13):
                    
                    showFret(1,i)
                
            if event.key == pg.K_2:
                
                for position in E_list:
                    
                    showFret(position[0], position[1])
                    
                    
            if event.key == pg.K_3:
                
                for note in list_of_lists:
                    
                    for position in note:
                        
                        showFret(position[0], position[1])
                
             
                
            if event.key == pg.K_SPACE:
                
                reset()
                
                
                
            if event.key == pg.K_c:
                
                showFret(6,8)
                


          
            
print("You quit the loop")          
pg.quit()


        




























