

activeZones = {}

def add_active_zone(zone, x, y):
	global activeZones
	activeZones[make_room_key(x, y)] = zone

def make_room_key(x, y):
	return str(x) + "," + str(y)