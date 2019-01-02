from tkinter import * # Importamos los widgets de Tkinter

def About():
    print ("This game is under GPL License. Developed by MAInformatico")

def imprimir(texto): print ("text") # Imprime un texto

root = Tk() # Creamos la raíz y se crea un bucle 
root.title("Rock Paper Scissors Lizard Spock")
root.geometry("800x600")
root.resizable(1,1) # Como si fueran 0 = False y 1 = True
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
label = Label(root, text="¡Otra etiqueta!")
label.pack(anchor="center")
label.config(bg="white", fg="blue", font=("Arial",24))
label.config(textvariable=text)

#Output results
textos = Text(root)
textos.pack(side="top")
textos.config(width=15, height=5, font=("Arial",15), padx=10, pady=5) # Aquí no son pixeles, si no caracteres

#Buttons player 1
Button(root, text="Rock", command=lambda: imprimir("Rock")).pack(side="left")
Button(root, text="Paper", command=lambda: imprimir("Paper")).pack(side="left")
Button(root, text="Scissors", command=lambda: imprimir("Scissors")).pack(side="left")
Button(root, text="Lizard", command=lambda: imprimir("Lizard")).pack(side="left")
Button(root, text="Spock", command=lambda: imprimir("Spock")).pack(side="left")

#Buttons player 2
Button(root, text="Rock", command=lambda: imprimir("0")).pack(side="right")
Button(root, text="Paper", command=lambda: imprimir("1")).pack(side="right")
Button(root, text="Scissors", command=lambda: imprimir("2")).pack(side="right")
Button(root, text="Lizard", command=lambda: imprimir("3")).pack(side="right")
Button(root, text="Spock", command=lambda: imprimir("4")).pack(side="right")



root.mainloop() # Cerramos el bucle , siempre al final del script
