from tkinter import *

def About():
    print ("This game is under GPL License. Developed by MAInformatico")

def imprimir(t): print (t) # Imprime un texto

root = Tk() # Creamos la raíz y se crea un bucle 
root.title("Rock Paper Scissors Lizard Spock")
root.geometry("800x600")
root.resizable(0,0) # Como si fueran 0 = False y 1 = True
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Exit", command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=About)


#dinamic vars
text = StringVar()
text.set("Rock, Paper, Scissors, Lizard, Spock Game!")
n1 = StringVar()
n2 = StringVar()

#Main title
label = Label(root, text=text.get())
label.pack(anchor="center")
label.config(bg="white", fg="blue", font=("Arial",24))

#Output results
textos = Text(root)
textos.pack(anchor="center", side="top")
textos.config(width=15, height=1, font=("Arial",20), padx=10, pady=5) # Aquí no son pixeles, si no caracteres

#Buttons player 1
label = Label(root, text="Player 1										Player2")
label.pack(side="bottom")
label.config(fg="blue", font=("Arial",12))
Button(root, text="Rock", command=lambda: imprimir("Rock")).pack(side="left")
Button(root, text="Paper", command=lambda: imprimir("Paper")).pack(side="left")
Button(root, text="Scissors", command=lambda: imprimir("Scissors")).pack(side="left")
Button(root, text="Lizard", command=lambda: imprimir("Lizard")).pack(side="left")
Button(root, text="Spock", command=lambda: imprimir("Spock")).pack(side="left")

#Buttons player 2
Button(root, text="Rock", command=lambda: imprimir("Rock")).pack(side="right")
Button(root, text="Paper", command=lambda: imprimir("Paper")).pack(side="right")
Button(root, text="Scissors", command=lambda: imprimir("Scissors")).pack(side="right")
Button(root, text="Lizard", command=lambda: imprimir("Lizard")).pack(side="right")
Button(root, text="Spock", command=lambda: imprimir("Spock")).pack(side="right")



root.mainloop() # Cerramos el bucle , siempre al final del script
