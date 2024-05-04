
import pygame
import sys
import random as rrr
from colors import changelist, colorlist as cl






# Colors 
WHITE = (0,0,0)
Dark =(73, 36, 62)######<------ RED MEANS STARTINGGG COLOR. SHOULD BE DARK
Light =(219, 175, 160)### <<______------ GREEEN MEANS ENDING COLOR. SHOULD BE BRIGHT
 

def colonizer(col1,col2):
    # Dark =(73, 36, 62)######<------ RED MEANS STARTINGGG COLOR. SHOULD BE DARK
    Dark =col1   ######<------ RED MEANS STARTINGGG COLOR. SHOULD BE DARK
    Light =(219, 175, 160)### <<______------ GREEEN MEANS ENDING COLOR. SHOULD BE BRIGHT
    Light =col2###<<______------ GREEEN MEANS ENDING COLOR. SHOULD BE BRIGHT
 

    num_squares = 12
    cl = []
    for i in range(num_squares + 2): 
        ratio = i / (num_squares + 1)
        r = int((1 - ratio) * Dark[0] + ratio * Light[0])
        g = int((1 - ratio) * Dark[1] + ratio * Light[1])
        b = int((1 - ratio) * Dark[2] + ratio * Light[2])
        cl.append((r, g, b))
        changelist(cl)
    print(cl)
    
def diffuser(col1,col2):
    # Dark =(73, 36, 62)######<------ RED MEANS STARTINGGG COLOR. SHOULD BE DARK
    Dark =col1   ######<------ RED MEANS STARTINGGG COLOR. SHOULD BE DARK
    Light =(219, 175, 160)### <<______------ GREEEN MEANS ENDING COLOR. SHOULD BE BRIGHT
    Light =col2###<<______------ GREEEN MEANS ENDING COLOR. SHOULD BE BRIGHT
 

    num_squares = 30
    cl = []
    for i in range(num_squares + 2): 
        ratio = i / (num_squares + 1)
        r = int((1 - ratio) * Dark[0] + ratio * Light[0])
        g = int((1 - ratio) * Dark[1] + ratio * Light[1])
        b = int((1 - ratio) * Dark[2] + ratio * Light[2])
        cl.append((r, g, b))
    return cl    
    