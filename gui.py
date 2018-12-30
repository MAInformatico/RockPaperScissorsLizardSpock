from Tkinter import *

def NewFile():
    print "New File!"
    print name
def About():
    print "This game is under GPL License. Developed by MAInformatico"
    
root = Tk()
root.geometry("800x600")
root.title('Rock, Paper, Scissors, Lizard, Spock')
root.config(bg="white")
widget = Label(None, text='Welcome to the game, have fun!', bg='white', fg = 'blue', font=('Ravie', 24))
widget.pack()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New game", command=NewFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=About)

#b1=Button(root,text="")
b1=Button(root,text="Start",command=lambda: ejecutar(mostrar(root)) or imprimir("hi"))
b1.pack() 

def imprimir(texto): print "text" # Imprime un texto




mainloop()
