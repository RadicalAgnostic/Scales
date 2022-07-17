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
    
Get the fretboard to print correctly the first time
Get text in circles to change with string distance
Rgb to hsv to fade color in circles

Show one position at a time
Show the names of notes
Show the relation of notes
Allow user to click notes
Type in key or something


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


    mouse_x, mouse_y = pg.mouse.get_pos()

    message = "Mouse x: " + str(mousex) +  " Mouse y:" + str(mousey)
    window.blit(font.render(message, True, text_color), (10, 30))
        
    pg.display.update()




"""
Here are the variables for initialization
"""


### Random stuff ###

purple = (200, 120, 212)  
cyan = (0, 240, 255)  
black = (0,0,0)
white = (255,255,255)
tan = (255,244,193)



### Creates window ###

window_length = 1000
window_height = 700

window_size = (window_length, window_height)
window = pg.display.set_mode((window_size), pg.RESIZABLE)
pg.display.set_caption("Funky Scale Time")

font = pg.font.SysFont("Sans", 20)
title_font = pg.font.SysFont("Sans", 77)
text_color = (black)

window.fill(tan)
pg.display.flip()



  
distance_from_window_to_frets = 100 * 2 

fret_length = (window_length - distance_from_window_to_frets) /12
string_distance = 50  


def reset():
    
    window.fill(tan)
    
    window.blit(title_font.render("FUNKY SCALE TIME", True, black), (120, 10))
    
    pg.draw.line(window, black, (100, 93), (100, 107 + 5*string_distance), 7)
    
    
    for i in range(0,6):
        pg.draw.line(window, black, (100, 100 + i*string_distance), (window_size[0]-100, 100 + i*string_distance), 2)
    
    for i in range(0,13):
        pg.draw.line(window, black, (100 + i*fret_length, 100), (100 + i*fret_length, 100 + 5 * string_distance), 2)
        
        
    drawCircle(black, (100 + (fret_length * 2.5), 101 + 2.5 * string_distance), 5, 1, black, 0)
    drawCircle(black, (100 + (fret_length * 4.5), 101 + 2.5 * string_distance), 5, 1, black, 0)
    drawCircle(black, (100 + (fret_length * 6.5), 101 + 2.5 * string_distance), 5, 1, black, 0)
    drawCircle(black, (100 + (fret_length * 8.5), 101 + 2.5 * string_distance), 5, 1, black, 0)
    
    drawCircle(black, (100 + (fret_length * 11.5), 101 + 1.5 * string_distance), 5, 1, black, 0)
    drawCircle(black, (100 + (fret_length * 11.5), 101 + 3.5 * string_distance), 5, 1, black, 0)
    
        
        
    open_notes = "eBGDAE"
    i = 0 
    for char in open_notes:
        
        window.blit(font.render(char, True, black), (73, 93 + (string_distance - 1)*i))
        i += 1
        

    
    fret_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    i = 0
    for char in fret_numbers:
        
        window.blit(font.render(char, True, black), 
                    (95 + (0.5 + i) * fret_length, 111 + (5) * string_distance))
        i += 1
    
    
    pg.display.flip()






def showFret(string, fret, radius = 12, color = white, text = ""):
    
    string -= 1
    
    
    if fret == 0:
        position = (101 + fret*fret_length, 101 + string*string_distance)
    else:
        fret -= 1
        position = (101 + (fret_length * .5) + fret*fret_length, 101 + string*string_distance)

    drawCircle(color, position, radius, 2, black, 0)
    
    
    window.blit(font.render(text, True, black), (position[0] - 6, position[1] - 13))
    
    
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


A_minor = [A_list, B_list, C_list, D_list, E_list, F_list, G_list]






note_positions_e = []

for i in range(13):
    
    100 + (fret_length * 0.5)
    
    
    
    print(i)


















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
                    
                    showFret(1,i, color = purple)
                
            if event.key == pg.K_2:
                
                for position in E_list:
                    
                    showFret(position[0], position[1], text = "e")
                    
                    
            if event.key == pg.K_3:
                
                for note in list_of_lists:
                    
                    for position in note:
                        
                        showFret(position[0], position[1])
                        
            if event.key == pg.K_a:
                
                for note in A_minor:
                    
                    for position in note:
                        
                        showFret(position[0], position[1], color = purple)
                
             
                
            if event.key == pg.K_SPACE:
                
                reset()
                
                
                
            if event.key == pg.K_c:
                
                showTime()
                


          








        elif event.type == pg.MOUSEBUTTONDOWN:
            
            mouse_x, mouse_y = pg.mouse.get_pos()
            
            # print(mouse_x, mouse_y)
            
            
            
            
            if abs(mouse_y - 100) < string_distance/2:
                
                print("you are on the e string")
                string = 1
                
            if abs(mouse_y - (100 + string_distance*1)) < string_distance/2:
                
                print("you are on the B string")
                string = 2
                
            if abs(mouse_y - (100 + string_distance*2)) < string_distance/2:
                
                print("you are on the G string")
                string = 3
                
            if abs(mouse_y - (100 + string_distance*3)) < string_distance/2:
                
                print("you are on the D string")
                string = 4
                
            if abs(mouse_y - (100 + string_distance*4)) < string_distance/2:
                
                print("you are on the A string")
                string = 5
            
            if abs(mouse_y - (100 + string_distance*5)) < string_distance/2:
                
                print("you are on the E string")
                string = 6
        
        
        
            if mouse_x > 75 and mouse_x  < 120:
                
                print("you are on the neck")
                fret = 0
                
            elif mouse_x < 100 + (fret_length*1):
                
                print("you are on fret 1")
                fret = 1
                
            elif mouse_x < 100 + (fret_length*2):
                
                print("you are on fret 2")
                fret = 2
                
            elif mouse_x < 100 + (fret_length*3):
                
                print("you are on fret 3")
                fret = 3
                
            elif mouse_x < 100 + (fret_length*4):
                
                print("you are on fret 4")
                fret = 4
                
            elif mouse_x < 100 + (fret_length*5):
                
                print("you are on fret 5")
                fret = 5
                
            elif mouse_x < 100 + (fret_length*6):
                
                print("you are on fret 6")
                fret = 6
                
            elif mouse_x < 100 + (fret_length*7):
                
                print("you are on fret 7")
                fret = 7
                
            elif mouse_x < 100 + (fret_length*8):
                
                print("you are on fret 8")
                fret = 8
                
            elif mouse_x < 100 + (fret_length*9):
                
                print("you are on fret 9")
                fret = 9
                
            elif mouse_x < 100 + (fret_length*10):
                
                print("you are on fret 10")
                fret = 10
                
            elif mouse_x < 100 + (fret_length*11):
                
                print("you are on fret 11")
                fret = 11
                
            elif mouse_x < 100 + (fret_length*12):
                
                print("you are on fret 12")
                fret = 12
        
        
        
        
        
            showFret(string, fret)
        
        
        
        
        
print("You quit the loop")          
pg.quit()


        
















