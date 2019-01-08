#!/usr/bin/python

import random

def Game(jug1,jug2):
	if jug1==v[0]:
		rock(jug1,jug2)
	else:
		if jug1==v[1]:
			paper(jug1,jug2)
		else:
			if jug1==v[2]:
				scissors(jug1,jug2)
			else:
				if jug1==v[3]:
					Lizard(jug1,jug2)
				else:
					if jug1==v[4]:
						spock(jug1,jug2)

#Game rules
def rock(jug1,jug2):
		if jug2==v[3]:
			print ("Rock lapida Lizard")
		else:
			if jug2==v[2]:
				print ("Rock crusher scissors")
			else:		#defeat
				if jug2==v[1]:
					print ("Paper cover rock")
				else:
					if jug2==v[4]:
						print ("Spock vaporizes rock")
					else:
						if jug1==v[0] and jug2==v[0]:
							print ("Draw")


def paper(jug1,jug2):
		if jug2==v[0]:
			print ("Paper cover rock")
		else:
			if jug2==v[4]:
				print ("Paper desauthorizes Spock")
			else:		#defeat
				if jug2==v[2]:
					print ("Scissors cuts paper")
				else:
					if jug2==v[3]:
						print ("Lizard eats paper")
					else:
						if jug1==v[1] and jug2==v[1]:
							print ("Draw")


def scissors(jug1,jug2):
		if jug2==v[3]:
			print ("Scissors decapitates Lizard")
		else:
			if jug2==v[1]:
				print ("Scissors cuts paper")
			else:		#defeat
				if jug2==v[0]:
					print ("Rock crusher scissors")
				else:
					if jug2==v[4]:
						print ("Spock rompe scissors")
					else:
						if jug1==v[2] and jug2==v[2]:
							print ("Draw")

def Lizard(jug1,jug2):
		if jug2==v[1]:
			print ("Lizard eats paper")
		else:
			if jug2==v[4]:
				print ("Lizard poison Spock")
			else:		#defeat
				if jug2==v[2]:
					print ("Scissors decapitates Lizard")
				else:
					if jug2==v[0]:
						print ("Rock lapida Lizard")
					else:
						if jug1==v[3] and jug2==v[3]:
							print ("Draw")

def spock(jug1,jug2):
		if jug2==v[0]:
			print ("Spock vaporizes rock")
		else:
			if jug2==v[2]:
				print ("Spock breaks scissors")
			else:		#defeat
				if jug2==v[1]:
					print ("Paper desauthorized Spock")
				else:
					if jug2==v[3]:
						print ("Lizard poison Spock")
					else:
						if jug1==v[4] and jug2==v[4]:
							print ("Draw")


if __name__ == "__main__":
	v=['rock','paper','scissors','lizard','Spock']
	ajug=int(input("Press the number key corresponding to the selected weapon: (0) Rock | (1) Paper | (2) Scissors | (3) Lizard | (4) Spock "))
	jug1=v[ajug]
	def aleatoria(v):
		b=random.randint(0, 4)
		return b

	a=aleatoria(v)
	jug2=v[a]
	Game(jug1,jug2)