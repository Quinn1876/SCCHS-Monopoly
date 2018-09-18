import random


class Card:
	"""
	General functions of every card(space in the game)
	"""
	def getType(self):
		return self.Type

	def getName(self):
		return self.Name

	def getID(self):
		return self.ID


class GameTile(Card):
	"""--Type: railway, utility, property 
	--Cost:price to buy --Rent: list of all rent prices 
	--House: House price 
	--Colour: Colour fam that it belongs to 
	--Morgage: the morgage price 
	--Name: Name of the card
	"""

	def __init__(self, T, C,  R, H, Cr, M, N, I):
		self.Type = T
		self.Cost = C
		self.Rent = R
		self.House = H	
		self.Colour = Cr
		self.Morgage = M 
		self.Name = N
		self.ID = I
		
	
	def getCost(self, House = None):
		"""
		If the parameter is left blank, then it will return the cost of the property
		IF the Parameter is not left as None, then it will return the Cost of the House
		"""

		if House is not None:
			return self.House
		else:
			return self.Cost
		
	# --nProperty is an int for the number of properties --nHouse is an int for the number of houses --Hotel is a boolean which is true if you own a hotel on it 
	def getRent(self, nProperty, nHouse = 0, Hotel = False):
		"""
		nProperty -- The number of that type of proerties owned
		nHouse -- The number of houses on the property DEFAULT - 0
		Hotel -- True if there is a hotel on the Property DEFAULT - False
		"""

		if self.Type.lower() == 'railway':
			return self.Rent[nProperty - 1]
			
		elif self.Type.lower() == 'utlity':
			if nProperty == 1:
				return random.randint(1,6) * 4 
			elif nProperty == 2:
				return random.randint(1,6) * 10	
				
		elif self.Type.lower() == 'property':
			if nProperty in range(1,3):
				return self.Rent[0]
			elif nProperty == 3:
				if nHouse == 0:
					return self.Rent[0] * 2
				elif nHouse in range(1,5):
					if Hotel == True:
						return self.Rent[5]
					else:
						return self.Rent[nHouse]
						
	def getColour(self):
		"""
		Returns the colour of the property
		"""

		if self.Type == 'property':
			return self.Colour
		else:
			return 'no colour'
		
	
		
class Tax(Card):
	"""
	Tax spaces on the board
	Card 5 
	Card 39
	"""

	def __init__(self, t, n, p, i):
		self.Type = t
		self.Name = n
		self.ID = i
		self.Price = p
		
	def getPrice(self):
		return self.Price
		
class Other(Card):
	"""
	The four corner spaces
	Card 1 
	Card 11
	Card 21
	Card 31
	"""

	def __init__(self, t, name, i):
		self.Name = name
		self.ID = i
		self.Type = t
		
	


class Blank(Card):
	"""
	Any Blank space that has nothing 
	"""

	def __init__(self, ID):
		self.ID = ID
		self.Name = 'Blank'
		self.Type = 'Blank'