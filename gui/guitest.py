from easygui import *
import sys
cart1=[]
cart2=[]
s=0
msgbox('welcome to gamers')
while 1:
   c0=buttonbox('types of games','online games',('pubg','cod','fortnite'))
   if c0=='pubg':
     o={'pochinki=$15':15,'school=$20':20,'military base=$5':5}
     c1=choicebox('suicide spots','pubg',o)
     c2=o[c1]
     cart1.append(c1)
     cart2.append(c2)

   elif c0=='cod':
     o={'popcorn=$15':15,'chai=$20':20,'parle=$5':5}
     c1=choicebox('hungry try this','cod',o)
     c2=o[c1]
     cart1.append(c1)
     cart2.append(c2)
   pcart2=print(sum(cart2))

   msg = "continue shopping?"
   title = "Please Confirm"
   if ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
   else:
       msgbox("in your cart:" + str(cart1) + '\n' + 'plz pay amount : $'+ str(sum(cart2)))
       #sys.exit(0)
 
    
