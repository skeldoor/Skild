class Character(object):
	
	def __init__(self, xposition, yposition, width, height, model, colour, speed, direction):
		self.xposition = xposition
		self.yposition = yposition
		self.width = width
		self.height = height
		self.model = model
		self.colour = colour
		self.speed = speed
		self.direction = direction

	def update(self):
		if self.direction == 1:
			self.yposition = self.yposition - self.speed
		elif self.direction == 2:
			self.xposition = self.xposition + self.speed
		elif self.direction == 3:
			self.yposition = self.yposition + self.speed
		elif self.direction == 4:
			self.xposition = self.xposition - self.speed