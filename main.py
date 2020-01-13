#Monopoly made by Quinn Hodges

import random
import time
import card
import player
import GameBoard

 
def main():
	introduction()
	playing = True
	board.draw(playerList)
	while playing:
		
		#  i is the player
		for i in playerList:
			
			#  checks if the player is broke and in the game
			if i.isPlaying() and i.getMoney() > 0 and playing:
				print('It is now ' + i.getName() + "'s turn.")
				
				#  continues to loop until the player rolls the dice
				roll = rollDice(i)

				print('You rolled a ' + str(roll))
				i.move(roll)
				time.sleep(3)
				#  board.draw(playerList)

				#  determines what space the player has landed on after rolling
				for a in MASTER_LIST:
					if a.getID() == i.getSpace():
						print(i.getName() + ' has landed on ' + a.getName())
						currentSpace = a
				
				
				########################################################################
				#        If the card is a tax card, then make the player pay for it    #
				if currentSpace.getType() == 'tax':
					print('You must pay the bank $' + str(currentSpace.getPrice()))
					time.sleep(1)

					if i.getMoney() >= currentSpace.getPrice():
						i.removeMoney(currentSpace.getPrice())
						print('You pay the bank $' + str(currentSpace.getPrice()))
						time.sleep(1)
					else:
						i.removeMoney(i.getMoney()) 
						i.isPlaying(False)
						print('You are unable to pay due to insufficient funds and therefore have lost.')
						checkWin()
					playing = False
					owner = 1
					
				#########################################################################
				# Tax cards do not have an owner                                       ##
				# So if it is not a tax card, then find the owner(Bank or a Player)    ##
				else:
					owner = getOwner(currentSpace.getID())
				

				#  If the player landing on the card does not own it
				if str(owner) != str(i.getNumber()) and playing:
					#  If the card is owned by the bank, they may buy it
					if str(owner) == 'bank':
						print(currentSpace.getName() + " is owned buy the bank. Would you like to buy it for $" + str(currentSpace.getCost()) + '?')
						choice = input()
						print('----------')

						#They buy the property if they have enough money and they want to buy it
						if choice.lower().startswith('y') and i.getMoney() >= currentSpace.getCost(): 
							i.addDeed(currentSpace)
							bankDeeds.remove(currentSpace)
							i.removeMoney(currentSpace.getCost())
							print('You have purched ' + currentSpace.getName())

						#They are unable to buy the property if they fo not have enough property
						if 	i.getMoney() < currentSpace.getCost():
							print('You do not have enough money to purchase this tile.')

						time.sleep(1)

					for p in playerList:
						if p.getNumber() == owner:
							print('This property is owned by ' + p.getName() + '. \nYou pay them ' + str(currentSpace.getRent(1,0,0)))
							
							# Player that lands on the space pays rent
							if i.getMoney() >= currentSpace.getRent(1,0,0): 
								i.removeMoney(currentSpace.getRent(1,0,0))
								p.addMoney(currentSpace.getRent(1,0,0))
							else:
								i.removeMoney(i.getMoney()) 
								i.isPlaying(False)
								print('You are unable to pay due to insufficient funds and therefore have lost.')	
								checkWin()
						
			time.sleep(1)		
			board.draw(playerList)
						
						
#Gets the number of players
def introduction():
	"""
	Welcome players to the Game.
	Adds players based on the number inputed
	Asks players for their name
	"""
	print('Welcome to Monopoly: \n\tSCCHS Edition')
	choice = getChoiceInt('How many people will be playing? (2-6)', 2, 6)
	for i in range(int(choice)):
		playerList.append(player.Human(i+1))
		playerList[i].isPlaying(True)
		playerList[i].setName(input('What is your name Player ' + str(i + 1) + '?\n'))
			
	choice = input('Would you like to view the instructions ')
	if choice.lower().startswith('y'):
		print('Players will take turns rolling the dice, moving on the board, buying properties, and paying/collecting rent.') 


def getOwner(space):
	"""
	Determines the owner of the property based on its ID
	Checks the bank, then checks players one by one
	"""
	for deed in bankDeeds:
		if deed.getID() == space:
			return 'bank'
	for p in playerList:
		if p.getDeeds('list') == []:
			break
		for deed in p.getDeeds('list'):
			if deed.getID() == space:
				return p.getNumber()


def checkWin():
	"""
	Checks to see if there is more than one player playing

	If only one player is playing, then they win
	"""
	global playing
	numPlayers = 0
	for i in playerList:
		if i.isPlaying(''):
			numPlayers += 1
	if numPlayers == 1:
		for i in playerList:
			if i.isPlaying(''):
				print(i.getName() + ' has won!')
				playing = False


def getChoiceInt(message, a, b):
	"""
	Getting a players input that has to be within a range of two numbers
	Includes lower and upper limmit
	Asks the player a given question

	a is the lower limmit
	b is the upper limmit
	x is the number intputed by the user
	"""

	try:
		x = int(input(message))
		if x in range(a, b + 1):
			return x
		else:
			return getChoiceInt(message, a, b)
	
	except ValueError:
		print('You must enter a single number.')
		return getChoiceInt(message, a, b)


def rollDice(player):
	"""
	A recursive function that waits for the dice roll.
	"""
	try:
		choice = int(input('What would you like to do?\n\t1. View inventory \n\t2. Roll the Die \n'))
	except ValueError:
		print('Please input a number')

	if choice == 1:
		print('----------')
		print(player.getName() + "'s Inventory: ")
		print("Money: " + str(player.getMoney()))
		print("Deeds: " + str(player.getDeeds('string')))
		return rollDice(player)
		
	elif choice == 2:
		print('----------')
		#rolls the dice
		roll1 = random.randint(1,6)
		roll2 = random.randint(1,6)
		tRoll = roll1 + roll2
		return tRoll
	
	else:
		return rollDice(player)	

	

#Purple Cards
card2 = card.GameTile('property', 60, [2, 10, 30, 90, 160, 250], 50, 'purple', 30, 'Grade 9 Math and Science', 2)
card4 = card.GameTile('property', 60, [4, 20, 60, 180, 320, 450], 50, 'purple', 30, 'Grade 9 English and History', 4)

#light-blue Cards
card7 = card.GameTile('property', 100, [6, 30, 90, 270, 400, 550], 50, 'light-blue', 50, 'Grade 10 English', 7)
card9 = card.GameTile('property', 100, [6, 30, 90, 270, 400, 550], 50, 'light-blue', 50, 'Grade 11 English', 9)
card10 = card.GameTile('property', 120, [8, 40, 100, 300, 450, 600], 50, 'light-blue', 60, 'Grade 12 English', 10)

#pink cards
card12 = card.GameTile('property', 140, [10, 50, 150, 450, 625, 750], 100, 'pink', 70, 'Grade 10 Workplace', 12)
card14 = card.GameTile('property', 140, [10, 50, 150, 450, 625, 750], 100, 'pink', 70, 'Grade 10 Foundations', 14)
card15 = card.GameTile('property', 160, [12, 60, 180, 500, 700, 900], 100, 'pink', 80, 'Grade 10 Science', 15)

#orange cards
card17 = card.GameTile('property', 180, [14, 70, 200, 550, 750, 950], 100, 'orange', 90, 'Foundations 20', 17)
card19 = card.GameTile('property', 180, [14, 70, 200, 550, 750, 950], 100, 'orange', 90, 'Worplace 20', 19)
card20 = card.GameTile('property', 200, [16, 80, 220, 600, 800, 1000], 100, 'orange', 100, 'Pre-Calculus 20', 20)

#red cards
card22 = card.GameTile('property', 220, [18, 90, 250, 700, 875, 1050], 150, 'red', 110, 'Health Science 20', 22)
card24 = card.GameTile('property', 220, [18, 90, 250, 700, 875, 1050], 150, 'red', 110, 'Environmental Science 20', 24)
card25 = card.GameTile('property', 240, [20, 100, 300, 750, 925, 1100], 150, 'red', 120, 'Physical Science 20', 25)

#yellow cards
card27 = card.GameTile('property', 260, [22, 110, 330, 800, 975, 1150], 150, 'yellow', 130, 'Chemistry 30', 27)
card28 = card.GameTile('property', 260, [22, 110, 330, 800, 975, 1150], 150, 'yellow', 130, 'Biology 30', 28)
card30 = card.GameTile('property', 280, [24, 120, 360, 850, 1025, 1200], 150, 'yellow', 140, 'Physics 30', 30)

#green cards
card32 = card.GameTile('property', 300, [26, 130, 390, 900, 1100, 1275], 200, 'green', 150, 'Foundations 30', 32)
card33 = card.GameTile('property', 300, [26, 130, 390, 900, 1100, 1275], 200, 'green', 150, 'Workplace 30', 33)
card35 = card.GameTile('property', 320, [28, 150, 450, 1000, 1200, 1400], 200, 'green', 160, 'Pre-Calculus 30', 35)

#blue cards
card38 = card.GameTile('property', 350, [35, 150, 500, 1100, 1300, 1500], 200, 'blue', 175, 'Computer Science 20', 38)
card40 = card.GameTile('property', 400, [50, 200, 600, 1400, 1700, 2000], 200, 'blue', 200, 'Computer Science 30', 40)

#utility cards
card13 = card.GameTile('utility', 150, 0, 0, '', 75, 'Library', 13)
card29 = card.GameTile('utility', 150, 0, 0, '', 75, 'Wifi Network', 29)

#railway cards
card6 = card.GameTile('railway', 200, [25, 50, 100, 200], 0, '', 100, 'Gym', 6)
card16 = card.GameTile('railway', 200, [25, 50, 100, 200], 0, '', 100, 'Science Labs', 16)
card26 = card.GameTile('railway', 200, [25, 50, 100, 200], 0, '', 100, 'Computer Labs', 26)
card36 = card.GameTile('railway', 200, [25, 50, 100, 200], 0, '', 100, 'Shop Hallway', 36)

#Tax cards 
card5 = card.Tax('tax', 'Registration Fees', 200, 5)
card39 = card.Tax('tax', 'AP Test', 75, 39)

#other cards
card1 = card.Other('other', "Home Room", 1)
card11 = card.Other('other', "Detention / Office", 11)
card21 = card.Other('other', "Free Parking", 21)
card31 = card.Other('other', "Go to Detention", 31)

#Blank Cards
card3 = card.Blank(3)
card8 = card.Blank(8)
card18 = card.Blank(18)
card23 = card.Blank(23)
card34 = card.Blank(34)
card37 = card.Blank(37)

#list of all cards
MASTER_LIST = [card1, card2, card3, card4, card5, card6, card7, card8, card9,
			  card10, card11, card12, card13, card14, card15, card16, card17,
			  card18, card19, card20, card21, card22, card23, card24, card25,
			  card26, card27, card28, card29, card30, card31, card32, card33,
			  card34, card35, card36, card37, card38, card39, card40]
#  A list of all the titles owned by the bank.
bankDeeds = [card2, card4, card6, card7, card9, card10, card12, card13, card14,
			card15, card16, card17, card19, card20, card22, card24, card25,
			card27, card26, card28, card29, card30, card32, card33, card35,
			card36, card38, card40]

board = GameBoard.board()
playerList = []

main()
