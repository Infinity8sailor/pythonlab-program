from easygui import *
import sys
while 1:
    msgbox("welcome to online shopping store")

    msg ="types of grocery "
    title = "currently available options"
    choices = ["chocalate", "biscuit", "soap", "clothes"]
    choice = buttonbox(msg, title, choices)
    if choice=='chocalate':
      msg1="types of chocalate"
      title1="available options"
      choices1=['perk','5 star']
      choice1=choicebox(msg1,title1,choices1)
    elif choice=='biscuit':
      msg1='types of bisciut'
      title1='available options'
      choices1=['oreo','parle','tiger']
      choice1=choicebox(msg1,title1,choices1)
    elif choice=='clothes'
:      msg1='clothes'
      title1='available options'
      choices1=['t-shirt','cap','jeans']
      choice1=choicebox(msg1,title1,choices1)
    else choice=='soap'
         msg1='soap brands'
         title1='available opyions'
         choices1=['santoor','dove','patanjali']
         choice1=choicebox(msg1,title1,choices1) 
  # note that we convert choice to string, in case
    # the user cancelled the choice, and we got None.
    msgbox("You chose: " + str(choice), "selected item")

    msg = "Do you want to continue?"
    title = "Please Confirm"
    if ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:
        sys.exit(0)

