# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 01:07:31 2020

@author: alvar
"""
# Import libraries
import csv
import re
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo

# Define Variables that we will need to store important data, and we want them to be accesible to every functions that needs them
lista = []
dicc = {}
file = ""
sel = None

# Define Functions
def semester():
    """ This function creates a csv-file asking the user for a name. If the user doesn't specify that it is a csv file, it does it automatically. 
    At the end, it opens the file created with a default value"""
    
    global lista
    global dicc
    global file
    
    # We need to clear the variables, to have just the information of the actual file.
    lista = []
    dicc = {}
    
    sub.set("")
    comments.delete('1.0',END)
    courses.delete(0,courses.size())
    
    file = asksaveasfilename(initialdir="/", filetypes=(("csv file","*.csv"),("All Files","*.*")),title="Save as")
    if re.search('\.csv$',file) == None and len(file) > 0:
        file += ".csv"
        
    start = ['name','comment','hours']    
    default = ['Subject',"Waiting for a comment","100"]
    
    try:
        with open(file,"w",newline="", encoding="utf-8") as fin:
            writer = csv.writer(fin, delimiter=";")
            writer.writerow(start); writer.writerow(default)
            
    except:
        print("Something went wrong while creating the file")
        
    else:
        showinfo("Information","The file has been created and opened successfully")
        
    try:
        with open(file, encoding="utf-8") as doc:
            content= list(csv.reader(doc, delimiter=";"))
        
        for i in range(1,len(content)):
            lista.append(content[i][0])
            if not content[i][0] in dicc:
                dicc[content[i][0]] = [content[i][1],content[i][2]]
               
    except:
        print("It was not possible to open the created file")
        
    display(dicc)
        
                                                                           
def load():
    """ It opens an existing file, and displays it to the frame"""
    
    global lista
    global dicc
    global file
    
    lista = []
    dicc = {}
    
    sub.set("")
    comments.delete('1.0',END)
    courses.delete(0,courses.size())   
    
    file = askopenfilename(initialdir="/", filetypes=(("csv file","*.csv"),("All Files","*.*")),title="Choose a file")
    
    try:
        with open(file, encoding="utf-8") as doc:
            content= list(csv.reader(doc, delimiter=";"))
        
        for i in range(1,len(content)):
            lista.append(content[i][0])
            if not content[i][0] in dicc:
                dicc[content[i][0]] = [content[i][1],content[i][2]]
                
    except:
        print("It was not possible to open the file")
        
    display(dicc)

def on_select(event):
    """ It gets the value of the selected item in the listbox, store it and display information according to it"""
    
    global sel
    
    sub.set("")
    comments.delete('1.0',END)
    
    sel = event.widget.curselection()
    
    #print(lista); print(sel)
    
    try:
        if lista[sel[0]] in dicc:
            name.insert(0,lista[sel[0]])
            comments.insert(END,dicc[lista[sel[0]]][0])
            scale.set(dicc[lista[sel[0]]][1])
    except:
        pass
    #print(sub.get())
    
def keep_select():
    sub.set("")
    comments.delete('1.0',END)
    
    try:
        if lista[sel[0]] in dicc:
            name.insert(0,lista[sel[0]])
            comments.insert(END,dicc[lista[sel[0]]][0])
            scale.set(dicc[lista[sel[0]]][1])
    except:
        pass
    
def display(dicc):
    """ It takes the data stored in the file and displays it"""
    
    sub.set("")
    comments.delete('1.0',END)
    courses.delete(0,courses.size())
    
    for key in lista:
        courses.insert(END,key)
    
    for key in dicc:
        name.insert(0, key)
        scale.set(dicc[key][1]) 
        comments.insert(END, dicc[key][0])
        break;
        
    print("diccionario: \n",dicc); print("lista: \n", lista)
    
    
def modify_name(event):
    """ It saves the new name of the subject, stores it and deletes the previous one"""
    
    global lista
    global dicc
    global sel
    
    # lista[sel[0]]  Value of the selected subject
    try:
        if sub.get() not in dicc:
            if lista[sel[0]] in dicc:
                dicc[sub.get()] = dicc[lista[sel[0]]]
                del dicc[lista[sel[0]]]
    
            for index, value in enumerate(lista):
                if value == lista[sel[0]]:
                    lista[index] = sub.get()            
        else:
            showinfo("Not possible","There is already one subject with that name")
    except:
        print("Remember to select a subject for being able to modify values")
            
            
    display(dicc)
    keep_select()
    
def modify_text(event):
    """ It saves the new comment of the subject, stores it and deletes the previous one"""
    
    global lista
    global dicc
    global sel
    
    # lista[sel[0]]  Value of the selected subject
    try:
        if lista[sel[0]] in dicc:
            dicc[sub.get()][0] = comments.get('1.0','end-1c')
    except:
        print("Remember to select a subject for being able to modify values")
            
            
    display(dicc)
    keep_select()
    
def modify_scale(event):
    """ It saves the new hours' value of the subject, stores it and deletes the previous one"""
    
    global lista
    global dicc
    global sel
    
    # lista[sel[0]]  Value of the selected subject
    try:
        if lista[sel[0]] in dicc:
            dicc[sub.get()][1] = scale.get()
    except:
        print("Remember to select a subject for being able to modify values")
                    
            
    display(dicc)
    keep_select()
        
def save():
    """ It takes the information on tkinter. If there is already a file opened it saves it, otherwise it creates a file asking the user for the name of the file"""
    
    global file
    
    start = ['name','comment','hours']   
    
    #If there is a file opened
    if file != "":
        with open(file,"w",newline="",encoding="utf-8") as fin:
            writer = csv.writer(fin, delimiter=";")
            writer.writerow(start)
            for key in dicc.keys():
                line = [key,dicc[key][0],dicc[key][1]]
                writer.writerow(line)
                
        showinfo("Information","The file has been saved successfully")
            
    #If there is no file opened
    else:
        file = asksaveasfilename(initialdir="/", filetypes=(("csv file","*.csv"),("All Files","*.*")),title="Save as")
        if re.search('\.csv$',file) == None and len(file) > 0:
            file += ".csv"
            
        with open(file,"w",newline="",encoding="utf-8") as fin:
            writer = csv.writer(fin, delimiter=";")
            writer.writerow(start)
            for key in dicc.keys():
                line = [key,dicc[key][0],dicc[key][1]]
                writer.writerow(line)
                
        showinfo("Information","The file has been created and saved successfully")
    
def add_course():
    """ Adds a course to the listbox, it is possible to add 30 new subjects with default values"""
    
    global dicc
    global lista
    
    number = [f"New Subject {i}" for i in range(1,31)]
    for i in range(len(number)):
        if number[i] not in dicc:
            dicc[number[i]] = ['Waiting for a comment','100']
            lista.append(number[i])
            break;
            
    display(dicc)
        
def delete_course():
    """ Deletes a course from the listbox, as well as in the objects where it was stored"""
    
    global dicc
    global lista
    global sel
    
    if sel:
        if lista[sel[0]] in dicc:
            del dicc[lista[sel[0]]]
            lista.remove(lista[sel[0]])
        
        
    display(dicc)        

def helps():
    showinfo("HELP","File --> New semester will create a new file where you can store data for a new semester\t \t \t\
             File --> Open will load an existing file and you will be able to see your saved data \t \t \t \t \
             File --> Save will store any changes into the existing file\
             File --> Exit will close the Tkinter tab \t\t \
             File --> Help will show you nothing new\n\n + To save the changes of the subject, click CONTROL \n\t \t \t \t \t")
    
# Create the root
root = Tk()
root.title("Informatics: My course Tracker")
root.geometry("1000x520+100+100")       #Pixels, Where the tab opens


# Define all of the variables for each GUI component
sub = StringVar()
sca = StringVar()

# Create the menu bar
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

# File Section
filemenu.add_command(label="New Semester", command=semester)
filemenu.add_command(label="Open", command=load)
filemenu.add_command(label="Save", command=save)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy)

# Help Section
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", command=helps)
root.config(menu=menubar)

# Add/delete courses
add_icon = PhotoImage(file="add.png")
add_button = Button(root, text="Add Course",image=add_icon, compound=LEFT, command=add_course)
add_button.grid(row=0, column=0)

del_icon = PhotoImage(file="delete.png")
del_button = Button(root, text="Delete Course",image=del_icon, compound=LEFT, command = delete_course)
del_button.grid(row=0, column=1)

#List of courses
courses = Listbox(root, width=30, height=26, borderwidth=2, relief="groove",exportselection=False) 
courses.grid(row=1, column=0, columnspan=2, rowspan=3, sticky=N+E+S+W)

scrollbar = Scrollbar(root, orient="vertical")
scrollbar.grid(row=1, column=1,columnspan=2, rowspan=3, sticky=N+S)


courses.bind('<<ListboxSelect>>', on_select)



courses.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=courses.yview)


# Entry for course name
label_name = Label(root, text="Course Name ")
label_name.grid(row=1, column=2)

name = Entry(root, width=107, textvariable=sub)
name.grid(row=1, column=3)

name.bind('<Control_L>',modify_name)

# Entry for comments
label_comments = Label(root, text="Comments ")
label_comments.grid(row=2, column=2)

comments = Text(root)
comments.grid(row=2, column=3)

comments.bind('<Control_L>',modify_text)

# Scale for my working hours
label_hours = Label(root, text="My working hours ")
label_hours.grid(row=4, column=2)

scale = Scale(root, from_=0, to=200, orient=HORIZONTAL, length=500, variable=sca)
scale.grid(row=4, column=3)

scale.bind('<ButtonRelease-1>', modify_scale)



mainloop()