import tkinter as tk
from tkinter import *
from random import randint
#Creating root and renaming Tk as tk, Naming the window and also how big it will be
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("500x300")

def new_rand():
    #Clears entry box
    pw_entry.delete(0, END)
    #Get password length and conver to int
    pw_len = int(my_entry.get())

    #Create variable to hold pass
    my_pass = ''

    for x in range(pw_len):
        my_pass += chr(randint(33,126))

    #Output password to screen
    pw_entry.insert(0, my_pass)

#Copy function
def copy():
    #Clears the clipboard
    root.clipboard_clear()
    #Copys to the clipboard
    root.clipboard_append(pw_entry.get())

#Generating random askii text between 33,126. 
my_pass = chr(randint(33,126))

#Label Frame
label = LabelFrame(root, text="How Many Characters?")
label.pack(pady=20) #Imports the label and gives it a position

#Creating an entry box to ask user the number of characters they would like the password to be
my_entry = Entry(label, font=("Helvetica", 24))
my_entry.pack(pady=20, padx=20)

#creating an entry box for returned password.
pw_entry = Entry(root, text = '', font=("Helvetica", 24), bd=0, bg="systembuttonface")
pw_entry.pack(pady=20)

#Create frame for buttons
my_frame = Frame(root)
my_frame.pack(pady = 20)

##Create buttons
my_button = Button(my_frame, text="Generate Random Password", command = new_rand)
my_button.grid(row = 0, column = 0, padx = 10)
copy = Button(my_frame, text = "Copy to clipboard", command = copy)
copy.grid(row = 0, column = 1, padx = 10)




root.mainloop()









