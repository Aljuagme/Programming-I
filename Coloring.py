# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 11:38:50 2019

@author: alvar
"""

def convert(color):
    try:
        if len(color) != 7:
            return("The input didn't have a proper length")
            
        
        # We set every posible hexagesimal number in integer
        dicc = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
        
        #We get sure that it is a valid Hex number
        for i in range(6):           
            if color[i+1] not in dicc:
                return(f"{color} is not a valid Hex color")
        #We assign the numbers to rgb
        red = (dicc[color[1]] *16**1) + (dicc[color[2]] *16**0)
        green = (dicc[color[3]] *16**1) + (dicc[color[4]] *16**0)
        blue = (dicc[color[5]] *16**1) + (dicc[color[6]] *16**0)
        
        print('"{}" = rgb({},{},{})'.format(color,red,green,blue))
        
        #We get new variables for cmyk
        red_prima = (red/255)
        green_prima = (green/255)
        blue_prima = (blue/255)
        
        #Formulas for cymk
        
        black=1-max(red_prima,green_prima,blue_prima)
        cyan=round(100*(1 - (red_prima) - black) / (1 - black))
        magenta=round(100*(1 - (green_prima) - black) / (1 - black))
        yellow=round(100*(1 - (blue_prima) - black) / (1 - black))
        
        #We round black at the end, like this is more accurate
        black = round(black*100)
        
        #print(cyan,magenta,yellow,black)
        return ('"{}" = cmyk({},{},{},{})'.format(color,cyan,magenta,yellow,black))
        
        
    except Exception:
        return("Oops, something went wrong")
        
color=input("Tell me a color in Hex format (i.e #001122): ")
print(convert(color))