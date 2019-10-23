from character import Character
class Player(Character):
	
	def __init__(self, xposition, yposition, width, height, model, colour, name, speed, direction, connection):
		super().__init__(xposition, yposition, width, height, model, colour, speed, direction)
		self.name = name
		self.connection = connection

	def update(self):
		super().update()