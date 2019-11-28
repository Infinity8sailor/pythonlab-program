import tkinter as vd
from tkinter import *
r=Tk()

var1=IntVar()
b=Checkbutton(r,text='music',variable=var1,fg='green',bg='red')
b.pack(side=RIGHT)
var2=IntVar()
c=Checkbutton(r,text='video',variable=var2)
c.pack(side=LEFT)

t=Text(r,height=20,width=20)
t.insert(start,'ffgjhgugu')
t.insert(END,'jsbvsjavvbbd')
t.pack(side=TOP)
r.mainloop()
