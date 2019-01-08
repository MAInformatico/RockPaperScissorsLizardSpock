from tkinter import *

def Game(jug1,jug2):
	if jug1==0:
		rock(jug1,jug2)
	else:
		if jug1==1:
			paper(jug1,jug2)
		else:
			if jug1==2:
				scissors(jug1,jug2)
			else:
				if jug1==3:
					lizard(jug1,jug2)
				else:
					if jug1==4:
						spock(jug1,jug2)

#Game rules
def rock(jug1,jug2):
		if jug2==3:
			print ("Rock lapida Lizard")
		else:
			if jug2==2:
				print ("Rock crusher scissors")
			else:		#defeat
				if jug2==1:
					print ("Paper cover rock")
				else:
					if jug2==4:
						print ("Spock vaporizes rock")
					else:
						if jug1==0 and jug2==0:
							print ("Draw")


def paper(jug1,jug2):
		if jug2==0:
			print ("Paper cover rock")
		else:
			if jug2==4:
				print ("Paper desauthorizes Spock")
			else:		#defeat
				if jug2==2:
					print ("Scissors cuts paper")
				else:
					if jug2==3:
						print ("Lizard eats paper")
					else:
						if jug1==1 and jug2==1:
							print ("Draw")


def scissors(jug1,jug2):
		if jug2==3:
			print ("Scissors decapitates Lizard")
		else:
			if jug2==1:
				print ("Scissors cuts paper")
			else:		#defeat
				if jug2==0:
					print ("Rock crusher scissors")
				else:
					if jug2==4:
						print ("Spock rompe scissors")
					else:
						if jug1==2 and jug2==2:
							print ("Draw")

def lizard(jug1,jug2):
		if jug2==1:
			print ("Lizard eats paper")
		else:
			if jug2==4:
				print ("Lizard poison Spock")
			else:		#defeat
				if jug2==2:
					print ("Scissors decapitates Lizard")
				else:
					if jug2==0:
						print ("Rock lapida Lizard")
					else:
						if jug1==3 and jug2==3:
							print ("Draw")

def spock(jug1,jug2):
		if jug2==0:
			print ("Spock vaporizes rock")
		else:
			if jug2==2:
				print ("Spock breaks scissors")
			else:		#defeat
				if jug2==1:
					print ("Paper desauthorized Spock")
				else:
					if jug2==3:
						print ("Lizard poison Spock")
					else:
						if jug1==4 and jug2==4:
							print ("Draw")


def about():
    print ("This game is under GPL License. Developed by MAInformatico")

def getWeapon(player, t):
	if player==1:
		jug1=t
		j[0]['state']="disabled"		
		j[1]['state']="disabled"
		j[2]['state']="disabled"
		j[3]['state']="disabled"
		j[4]['state']="disabled"
		print(t)
	else:
		jug2=t
		k[0]['state']="disabled"		
		k[1]['state']="disabled"
		k[2]['state']="disabled"
		k[3]['state']="disabled"
		k[4]['state']="disabled"		
		print(t)
		

if __name__ == "__main__":
	jug1=0
	jug2=0
	root = Tk()
	root.title("Rock Paper Scissors Lizard Spock")
	root.geometry("800x600")
	root.resizable(0,0)
	menu = Menu(root)
	root.config(menu=menu)
	filemenu = Menu(menu)
	menu.add_cascade(label="File", menu=filemenu)
	filemenu.add_command(label="Exit", command=root.quit)
	helpmenu = Menu(menu)
	menu.add_cascade(label="Help", menu=helpmenu)
	helpmenu.add_command(label="About", command=about)

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
	textos.config(width=15, height=1, font=("Arial",20), padx=10, pady=5)

	#Buttons player 1
	label = Label(root, text="Player 1										Player2")
	label.pack(side="bottom")
	label.config(fg="blue", font=("Arial",12))
	j=[ Button(root, state="active", text="Rock", command=lambda: getWeapon(1,0)),	
	Button(root, state="active", text="Paper", command=lambda: getWeapon(1,1)),	
	Button(root, state="active", text="Scissors", command=lambda: getWeapon(1,2)),	
	Button(root, state="active", text="Lizard", command=lambda: getWeapon(1,3)),
	Button(root, state="active", text="Spock", command=lambda: getWeapon(1,4)) ]
	#j[0]['state']="disabled"	
	j[0].pack(side="left")
	j[1].pack(side="left")
	j[2].pack(side="left")
	j[3].pack(side="left")
	j[4].pack(side="left")

	#Buttons player 2
	k=[ Button(root, state="active", text="Rock", command=lambda: getWeapon(2,0)),	
	Button(root, state="active", text="Paper", command=lambda: getWeapon(2,1)),	
	Button(root, state="active", text="Scissors", command=lambda: getWeapon(2,2)),	
	Button(root, state="active", text="Lizard", command=lambda: getWeapon(2,3)),
	Button(root, state="active", text="Spock", command=lambda: getWeapon(2,4)) ]
	#j[0]['state']="disabled"	
	k[0].pack(side="right")
	k[1].pack(side="right")
	k[2].pack(side="right")
	k[3].pack(side="right")
	k[4].pack(side="right")


root.mainloop()