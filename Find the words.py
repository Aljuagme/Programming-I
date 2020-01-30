# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 11:25:37 2019

@author: alvar
"""

def grid(word): 
    grid1 = ['CDNLOVEDMHCLOUD','ORIIMCHEANYTDDS','OAARHDRETMBHTCB','LMHADOOPHLEATAI','MACHINELEARNING','ADKINGSEMHSFSFD','TSCBYTEAAAEHTAA','PDOLYFTRTPCKACT','LZLJFRKNIPURTEA','OTBHAROICYREIBW','TSJHOHFNSSIMSOG','LOZWTSHGHGTSTOQ','IQTYDGANALYTICS','BEPANDASKKTLCZD','NZRBLOCKCHAISMF']

    # Search the word just in horizontal so we don't need a nested loop
    for i in range(len(grid1)):
        if grid1[i].count(word) == 1:
            return("{} found in location ({}, {}) in left to right direction".format(word,grid1[i].find(word),i))  #find etc position in that line, i = line
            
    # Search top to bottom, bottom to top
    for i in range(len(grid1)):
        palabra = ""            #We create the variable that it resets in every column
        for j in range(len(grid1[i])):
            palabra += grid1[j][i]
        if palabra.count(word) ==1: #We finish the loop, and search for the word in that column
            return("{} found in location ({}, {}) in top to bottom direction".format(word,i,palabra.find(word)))
        elif palabra[::-1].count(word) ==1:# And we search it backwards too
            return("{} found in location ({}, {}) in bottom to top direction".format(word,i,abs(palabra[::-1].find(word) -(len(grid1)-1)))) # if we do it backwards, the index would be the invers so, abs value of x -14

    # Search diagonal top to bottom
    for i in range(len(grid1)):
        palabra = ""
        #print(i)
        for j in range(len(grid1[i]) - i): #To avoid Index Error, we want the loop to last as long as letters are in there
            palabra += grid1[i+j][j]    # to start in every letter of the first column
            #print(palabra)
        if palabra.count(word) == 1:
            #print(palabra)
            return("{} found in location ({},{}) in diagonal top to bottom direction".format(word,palabra.find(word), i + palabra.find(word))) # It is in diagonal, so we want to "compensate" the desviation
     # Second half of the grid top to bottom 
    for i in range(len(grid1)):
        palabra = ""
        for j in range(len(grid1[i]) - i): 
            palabra += grid1[j][j+i] #to start in every letter of the first row
            #print(palabra)
        if palabra.count(word) == 1:
            return("{} found in location ({},{}) in diagonal top to bottom direction".format(word,i + palabra.find(word), palabra.find(word)))  
            
         
      #Search diagonal bottom to top 
    for i in range(len(grid1)-1,-1,-1):
        palabra = ""
        #print(i)
        for j in range(i+1):
           palabra += grid1[i-j][j]
           #print(palabra)
        if palabra.count(word) == 1:
            return("{} found in location ({}, {}) in diagonal bottom to top direction".format(word,palabra.find(word),j -palabra.find(word)))
        #print(palabra)
           
 # Search diagonal bottom to top second half

    for i in range(len(grid1)):
        palabra=""
        #print(i)
        for j in range(len(grid1[i]) -1 -i, -1,-1):
            palabra += grid1[j+i][len(grid1[i])-1-j]
            #print(palabra)
        #print(palabra)
        if palabra.count(word) == 1:
            return ("{} found in location ({}, {}) in diagonal bottom to top direction".format(word,palabra.find(word)+i, len(grid1) -1 -palabra.find(word)))
    return "Oops, I could not find {} in the grid".format(word)
        
word = input("Enter word to find: ")            
print(grid(word))  #If we put print the function, it will actually print the return, not just give it to you
    

    

    
      
