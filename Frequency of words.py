# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 21:36:32 2019

@author: alvar
"""

def wordCounter(fileName, length, n):
    lista = []
    diccionario = {}
    palabra = ""
    count = 0
    final = []
    try:
        with open(fileName,"r") as file:
            archivo = file.read()
            #print("printing archivo after reading: \n", archivo)
            for cha in archivo:
                #print("printing cha", ord(cha))
                if (ord(cha) >= 65 and ord(cha) <=90) or (ord(cha) >=97 and ord(cha) <=122):
                    palabra += cha
                    #print(palabra)
                elif len(palabra) > 0:
                    lista.append(palabra)
                    palabra=""
            #print("trying to print lista: \n", lista) 
            #print(len(lista))
            for i in range(len(lista)):
                #print("trying to print every value in lista: ", lista[i])
                if not lista[i] in diccionario:
                    diccionario[lista[i]] = 1
                else:
                    diccionario[lista[i]] +=1
        #print("printing la lista despues de meterle las palabras: \n", lista)
        #print("trying to print the diccionario \n", diccionario)
        
        for(key,value) in diccionario.items():
            if len(key) == length:
                final.append((key,value))
                final.sort(key=lambda elem:elem[1])   # We need lambda to specify the way we want to sort, the other way it's just append(value,key) but like this you learn 
                final.reverse()
                #print("trying to print final: ", final)
                
        for i in range(n):
            print(i+1,"\t", "\"{}\" : {}".format( final[i][0],final[i][1]))
            count += 1
            if count == len(final):
                break;
                

    except IOError:
       print("Sorry, could not find {}".format(fileName))
    except Exception:
        print("There is not a single word with this length")
    
    
    
wordCounter("test1.txt", 6, 8)
#wordCounter("test2.txt",8,3)


# Puedes resolverlo con 6 linias