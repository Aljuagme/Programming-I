# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 19:31:10 2019

@author: alvar
"""

def palindromic():
    count = 0
    try:
        n = int(input("Tell me a number: ")) #We ask the user for a number and we convert it into an integer 
        for i in range(n+1):
            i=str(i)                #Now we convert each number into a string to be able of reaching each ch
            if i[:]== i[::-1]:
                print(i)
                count += 1
            else:
                continue
        print("There are {} paleandromics numbers".format(count))
    except Exception:
        print("Give me an integer")
        palindromic()
        
       
palindromic()
