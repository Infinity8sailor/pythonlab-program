print('lets get started')
from tkinter import *
import tkinter as tk
import sys
import time
#import urllib.request
#from subprocess import Popen, PIPE, STDOUT
proj_num=0

class creator:
    def win_float():
        float_root=Tk()
        add_entry=tk.Entry(float_root)
        add_entry.grid(row=0,column=0)
        tk.Button(float_root,text='add_project',command=lambda : creator.add_project(add_entry.get())).grid(row=1,column=0)
        float_root.mainloop()
    
    def add_project(project_name):
        global proj_num
        tk.Label(login_page.pre_login.log.root,text=proj_num+1).grid(row=proj_num+1,column=0)
        tk.Label(log.root,text=project_name).grid(row=proj_num+1,column =1)
        proj_num+=1
class root_data():
    
    def __init__(self,root):
        self.root=root
        root.geometry('550x700+400+400')

        root.title("The interface")

        button=tk.Button(root,text='exit',command=exit)
        menubar=Menu(root,)

        GO=Menu(menubar,bg="green",tearoff=0,activebackground='red')
        online=Menu(menubar,tearoff=0)
        personal=Menu(menubar,tearoff=0)
    
        menubar.add_cascade(label='GO',menu=GO)
        menubar.add_cascade(label='online',menu=online)
        menubar.add_cascade(label='personal',menu=personal)

        GO.add_command(label='live',command=exit)
        GO.add_command(label='upcoming projects',command=exit)
        GO.add_command(label='vit',command=exit)
        GO.add_command(label='infinity',command=exit)
        GO.add_command(label="social",command=exit)
        online.add_command(label='insta',command=exit)
        online.add_command(label='website',command=exit)
        online.add_command(label='v-iot',command=exit)
        online.add_command(label='vit-database',command=exit)
        online.add_command(label="google",command=lambda: url('http://google.com'))
        personal.add_command(label='attitude',command=exit)
        personal.add_command(label='life goals',command=exit)
        personal.add_command(label='resume',command=exit)
        personal.add_command(label='GP',command=exit)
        personal.add_command(label="sop",command=exit)
    
        button.grid()
        root.config(menu=menubar)
        button=tk.Button(root,text="add project",command=creator.win_float)
        button.grid(row=0,column=0)

        root.mainloop()
        



        
        
        
def url(web):
    with urllib.request.urlopen(web) as response:
     html = response.read()
    test=Text(root)
    test.insert(INSERT,html)
    test.pack()
   
def ping_test():
    cmd = 'ping www.google.com'
    p = Popen(cmd.split(), stdout=PIPE, stderr=STDOUT)
    for line in iter(p.stdout.readline,''):
        ping = tk.Label(root, text=line)
        ping.pack()
  

class login_page:
    def __init__(self):
        pre_root=Tk()
        tk.Label(pre_root, text = "Username").grid(row = 0)
        user=tk.Entry(pre_root)
        user.grid(row=0,column=1)
        print("loop")
    
        tk.Label(pre_root,text="password").grid(row=1)
        pass_word=tk.Entry(pre_root)
        pass_word.grid(row=1,column=1)
        v1=IntVar()
        tk.Checkbutton(pre_root, text = "Keep Me Logged In", variable=v1).grid(columnspan = 2)
        tk.Button(pre_root,text='inter_now',command=lambda  : login_page.pre_login()).grid(row=3)
        pre_root.mainloop()
    
    
    def pre_login():
        if (user.get()=='cosmic'and pass_word.get()=="94210844")or(v1.get()==1):
           pre_root.destroy()
           log=root_data(Tk())
        else:
          pre_root.destroy()
          login_page()
login_page()





