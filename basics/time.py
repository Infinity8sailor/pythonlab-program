import tkinter as tk
from tkinter import *
  
counter = -1
running = False
def counter_label(label): 
    def count(): 
        if running: 
            global counter 
            if counter==-1:             
                display="Starting..."
            else: 
                display=str(counter) 
  
            label['text']=display   
            label.after(1000, count)  
            counter += 1
  
    
    count()      
  
def Start(label): 
    global running 
    running=True
    counter_label(label) 
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'
  

def Stop(): 
    global running 
    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'
    running = False
  

def Reset(label): 
    global counter 
    counter=-1
   
    if running==False:       
        reset['state']='disabled'
        label['text']='Welcome!'
  
    else:                
        label['text']='Starting...'
  
root = Tk() 
root.title("Stopwatch") 
  
# Fixing the window size. 
root.minsize(width=250, height=70) 
label = tk.Label(root, text="Welcome!", fg="black", font="Verdana 30 bold") 
label.pack() 
start = tk.Button(root, text='Start',  
width=15, command=lambda:Start(label)) 
stop = tk.Button(root, text='Stop',  
width=15, state='disabled', command=Stop) 
reset = tk.Button(root, text='Reset', 
 width=15, state='disabled', command=lambda:Reset(label)) 
start.pack() 
stop.pack() 
reset.pack() 
root.mainloop() 
