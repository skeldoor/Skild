class Zone(object):

	def __init__(self):
		self.zoneData = {}
		self.zoneCount = 0

	def add_zone(self, zone, x, y):
		self.zoneData[create_key(x, y)] = zone
		self.zoneCount = self.zoneCount + 1

	def create_key(x, y):
		return str(x) + "," + str(y)

	def spawn_new_zone(self, previousZone):
		if previousZone is None:
			spawn_start()
		elif previousZone.isConnector:
			spawn_arena(previousZone)
		elif previousZone.isArena:
			spawn_connector(previousZone)

	def spawn_start(self):
		print("start")