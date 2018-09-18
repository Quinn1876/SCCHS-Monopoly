class Human:
	def __init__(self, pNumber):
		self.Name = ''
		self.Number = pNumber
		self.Deeds = []
		self.Playing = False
		self.Money = 1500
		self.BoardSpace = 1
		self.InJail = False
	
	def isPlaying(self, arg1=None):
		if arg1 is True:
			self.Playing = True
		elif arg1 is False:
			self.Playing = False
		else:
			return self.Playing
	
	def addDeed(self, deed):
		self.Deeds.append(deed)
	
	def delDeed(self, deed):
		self.Deeds.remove(deed)
	
	def hasDeed(self, deed):
		for i in self.Deeds:
			if i == deed:
				return True
		return False
	
	def getDeeds(self, TYPE):
		if TYPE == 'string':
			string = ''
			for i in self.Deeds:
				string = string + i.getName() + '\n '
			return string
		if TYPE == "list":
			return self.Deeds
	
	def setName(self, name):
		self.Name = name
	
	def getName(self):
		return str(self.Name)
	
	def getMoney(self):
		return self.Money
	
	def addMoney(self, money):
		self.Money += money
	
	def removeMoney(self, money):
		self.Money -= money
	
	def getSpace(self):
		return self.BoardSpace
	
	def move(self, spaces):
		self.BoardSpace += spaces
		if self.BoardSpace > 40:
			print('You go to homeroom and collect $200.')
			self.BoardSpace -= 40
			self.Money += 200

	def getNumber(self):
		return self.Number
	
	def isInJail(self, arg1=None):
		if arg1 is True:
			self.InJail = True
		elif arg1 is False:
			self.InJail = False
		else:
			return self.InJail
	