class board:
	def __init__(self):
		"""
		Creates a game board based on the Base Board Text file
		"""
		self.board = []

		inFile = open('BaseBoard.txt', 'r')
		reader = inFile.readline()
		
		while reader:
			self.board.append(reader.rstrip('\n'))
			reader = inFile.readline()

		inFile.close()

	def draw(self, players):
		"""
		prints out the game board
		prints out each player and the space they are on

		****takes the list of players as an input
			Eventualy this will be replaced by placing the colour of the piece on the actual board spot
		"""

		for line in self.board:
			print(line)

		print('Name : Space')
		print('------------')
		for player in players:
			if player.isPlaying():
				print(player.getName() + ': ' + str(player.getSpace()))


