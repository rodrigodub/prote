#!/usr/bin/python

#################################################
## Main
## Rotina principal
## 
## v0.1.10
## for ticket ID57
## 
## Rodrigo Nobrega
## 20130827
#################################################



# import classes
from tkinter import *
# from Prote import *
from ProteGUI import *


# main loop
def main():  
	root = Tk()
	#root.geometry('700x400+100+100')
	root.title('Protê')
	app = ProteGUI(master=root)
	app.mainloop()
 

# main, calling main loop
if __name__ == '__main__':
    main()  










