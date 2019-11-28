from easygui import *
import sys
cart1=[]
cart2=[]
s=0
msgbox('welcome to our shop')
while 1:
  c0=buttonbox('MENU','ONLINE SHOP',('BEST SELLER','CAKES','SHAKES','SNACKS','PIZZA'))
  if c0=='BEST SELLER':    
     o={'cheese pizza=$150':150,'cadb=$50':50,'maggi=$25':25,'panner puf=$15':15}
     c1=choicebox('best selller products','online bakery',o)
     c2=o[c1]
     cart1.append(c1)
     cart2.append(c2)

  elif c0=='CAKES':
     o={'black forest=$200':200,'white frost=$200':200,'plain choclate cake=$125':125,'sugar free cake=$150':150}
     c1=choicebox('hungry try this','CAKES',o)
     c2=o[c1]
     cart1.append(c1)
     cart2.append(c2)
     
  elif c0=='SHAKES':
     o={'cadb=$50':50,'cold coffe=$25':25,'chocolate syrup=$30':30,'hot coffe=$15':15}
     c1=choicebox('hungry try this','SHAKES',o)
     
     c2=o[c1]
     cart1.append(c1)
     cart2.append(c2)
     
  elif c0=='SNAKES':
     o={'panner Puf=$15':15,'Sandwich=$20':20,'panneer roll=$15':15}
     c1=choicebox('hungry try this','cod',o)
     c2=o[c1]
     cart1.append(c1)
     cart2.append(c2)
     
  elif c0=='PIZZA':
     o={'cheese pizza=$150':150,'margherita pizza=$200':200,'chicken pizza=$250':250}
     c1=choicebox('hungry try this','PIZZA',o)
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
       sys.exit(0)
