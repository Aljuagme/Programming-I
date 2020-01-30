# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 10:29:13 2019

@author: alvar
"""  

lista = []     # Create a list to keep track of what I do before saving

def expense_tracker(action,filename):
    # Check what you want to do, and if you wrote correctly the command, if yes, call the other function           
    if action[0] == "-t":           
        if len(action) != 3: 
            return "The  number of arguments don't match for this command"
        return new_transaction(action[1], action[2])
            
    elif action[0] == "-d":
        if len(action) != 2:
            return "The number of arguments don't match for this command"
        return display(action[1],filename)
            
    elif action[0] ==  "-q":
        if len(action) != 1:
            return "The number of arguments don't match for this command"
        return log(filename)
    else:
        return "Wrong command"
                        
def new_transaction(amount, note):
    global balance              # I make global the variables due to the scope
    global transactions
    global lista
    
    # If you can afford it, keep going, change the balance and add 1 to the balance. Finally, append to the list, and say how much you have right now
    if (balance + float(amount)) >=0:
        balance += float(amount)
        transactions += 1
        #print("printing action in transaction: ", action)
        del action[0]
        #print("action after trying to get rid of the command", action)
        lista.append(action)

        return("OK, your balance is now {} Euros".format(balance))
                
    else:
        return("Sorry, can't spend more than you have!")
                
# I have work to do here        
def display(n, filename):
    n = int(n)
    show = []
    #print("printing lista", lista)
    if n < 0: return("invalid number")
    
    # I want to check the transactions that are already in the file, and get rid of the last one because splitting by \n, will give a last value of '" "' in the list
    with open(filename) as the_file:
        print("the_file", the_file)
        information = the_file.read().split("\n")
        information.pop()
        print("type of information1: ",type(information),"information", information)
        #For every transaction I did this time, I want to have it together with the ones that are saved in the file, so I put them together,
        # because lista is a list of lists, I access every lista, and inside, I make a join directly to append a string into information
    for i in range(len(lista)):
        information.append(" ".join(lista[i]))
        #print("type of information: ",type(information),"information", information)
    information.reverse()
    try:
        for i in range(n):
            show.append(information[i])
        show = "\n".join(show)
        return show
    except IndexError:
        return "There are not that amount of transactions yet"
            
def log(data):
    global lista
    with open(data,"a") as the_file:        # I take whatever I have in lista, and I append it to the file, and I empty lista for next time
        for i in range(len(lista)):
            print(lista[i][0] + " " + lista[i][1], file=the_file)       # also, print(" ".joint(lista[i]), file=the_file)
        lista = []
    # Once I wrote into the file, I change the variables of the other file, and I close the programm    
    with open("variables.txt",'w') as change:
        print("balance = {}".format(balance), file=change)
        print("transactions = {}".format(transactions),file=change)
    return "Saved status to {}! Bye!".format(data)
        

# Before starting, I take the variables to greed the user and tell him how much money there is,, according to the file,, if there is no file, I create it 
try:
    with open("variables.txt") as variables:
        variables = variables.read().split()
        balance = float(variables[2])
        transactions = int(variables[5])
except IOError:
    with open("variables.txt","w") as variables:
        print("balance = 0", file=variables)
        print("transactions = 0", file=variables)
        
    with open("variables.txt") as variables:
        variables = variables.read().split()
        balance = float(variables[2])
        transactions = int(variables[5])
        
# Create the file if it doesnt exist
try:
    with open("money.txt") as money:
        pass
except:
    with open("money.txt", 'w') as money:
        pass
        
print("Welcome" + "\n" + "Currently, your balance is {} Euros".format(balance))
print("There are {} transactions in your log file".format(transactions))
 
# I create a While loop for receiving inputs until it is saved   
while True:
     action = input("What do you want to do? type 'break' to exit without saving:  ")
     action = action.split(" ",2)
     #print("action", action)
     if action[0] == "break":
         break;
     print(expense_tracker(action,"money.txt"))
     if action[0] == "-q":
         break;
     