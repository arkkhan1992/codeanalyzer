import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import sys
from math import log2
import requests
from difflib import SequenceMatcher

def onclick():
    print("Button Clicked")
    newWindow = Toplevel(root)
    newWindow.geometry("550x400+650+250")
    newWindow.title("Check Similarity")
    newWindow.configure(background='White')
    
    Label = ttk.Label(newWindow, text = "Choose the file for Check The similarity", font=("Arial Bold", 10)).pack()
    
    button = ttk.Button(newWindow, text ="Browse A File",command = fileDialog).pack()
 
    
def fileDialog():
       
        filename = filedialog.askopenfilename( title = "Select A File", filetype =
        (("all files","*.*"),("java files","*.java"),("html files","*.html")) )
        newWindow = Toplevel(root)
        Label1 = ttk.Label(newWindow, text = "File : 1").place(x = 30,y = 50)
        Label2 = ttk.Label(newWindow, text = "File : 2").place(x = 30,y = 90)
        newWindow.geometry("550x400+650+250")
        newWindow.title("Similarity Output")
        newWindow.configure(background='White')
        Label = ttk.Label(newWindow, text = "")
        Label.place(relx=0.6,rely=0.2, anchor=CENTER)
        Label.config(text = filename)
        filename2 = filedialog.askopenfilename(initialdir = "/", title = "select A File", filetype = (("all files","*.*"),("java files",".java"),("html files",".html")))
        Label = ttk.Label(newWindow, text = "")
        Label.place(relx=0.6,rely=0.34, anchor=CENTER)
        Label.config(text = filename2)
    
        with open(filename) as file_1,open(filename2) as file_2:
                file1_data=filename
                file2_data=filename2
                similarity_ratio=SequenceMatcher(None,file1_data,file2_data).ratio()
        
                Label = ttk.Label(newWindow, text = "")
                Label.place(relx=0.6,rely=0.53, anchor=CENTER)
                Label.config(text =similarity_ratio)
                
                
def onclick2():
    print("Button Clicked")
    locWindow = Toplevel(root)
    locWindow.geometry("550x400+650+250")
    locWindow.title("Find the line of Code")
    locWindow.configure(background='White')
    
    Label = ttk.Label(locWindow, text = "Open File").pack()
    
    Label = ttk.Label(locWindow, text = "File 1:").place(x = 30,y = 50)
    
    Label2 = ttk.Label(locWindow, text = "LOC:").place(x = 30,y = 90)
    Label3 = ttk.Label(locWindow, text = "BLOC:").place(x = 30,y = 110)
    
    def fileDialog():
        filename = filedialog.askopenfilename( title = "Select A File", filetype =
        (("java files","*.java"),("html files","*.html")) )
        Label = ttk.Label(locWindow, text = "")
        Label.place(relx=0.6,rely=0.2, anchor=CENTER)
        Label.config(text = filename)
        
        
        num_lines = 0
        with open(filename, 'r') as f:
            for line in f:
                num_lines += 1
        Label = ttk.Label(locWindow, text = "")
        Label.place(relx=0.5,rely=0.33, anchor=CENTER)
        Label.config(text =num_lines)
        
        
        FILE_NAME = filename
        empty_line_count = 0
        with open(FILE_NAME, 'r') as fh:
            for line in fh:
                if line.split() == []:
                    empty_line_count += 1
        Label = ttk.Label(locWindow, text = "")
        Label.place(relx=0.5,rely=0.39, anchor=CENTER)
        Label.config(text =empty_line_count)
        
    button = ttk.Button(locWindow, text = "Browse a File",command = fileDialog).pack()


    

    
   

    
                
def onclick3():
    print("closed")
    root.destroy()

root = Tk()
root.geometry("550x400+650+250")
root.title("Code Analyzer System")
root.configure(background='White')

btn1=tk.Button(root,text="Similarity",width=20,height=2,command=onclick)

btn2=tk.Button(root,text="Find Line Of Code",width=20,height=2,command=onclick2)

btn3=tk.Button(root,text="Close",width=20,height=2,command=onclick3)
lbl = Label(root, text="Code Analyzer System", font=("Arial Bold", 30))
lbl1 = Label(root, text="by: Abdul Rehman Khan", font=("Arial Bold", 10))
#btn4 = Button(halsteadWindow, text="show",width=10,height=2,command=fileDialog).pack()
lbl.pack()
lbl1.pack()
btn1.pack()
btn2.pack()
btn3.pack()

#btn4.pack()
root.mainloop()
    
    