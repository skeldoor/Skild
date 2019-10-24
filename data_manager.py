

def parse_incoming(data):
	print(data)

def format_outgoing(blob):
	print(blob)

def format_keyframe(player, pm, gm):
	input = []
	input = create_kv(input, "px", player.x)
	input = create_kv(input, "py", player.y)
	input = create_kv(input, "map" serialise_map_data(gm))
	return ",".join(map(str, input))

def create_kv(input, key, value)
	newKv = key + ":" + str(value)
	return input.append(newKv)

def serialise_map_data(gm)
	mapData = []
	mapDict = gm.get_map()
	for zoneKey in mapDict:
		zone = mapDict[zoneKey]
		mapData.append(serialise_zone_data(zone))
	return "*".join(map(str, mapData))

def serialise_zone_data(zone):
	zoneData = []
	zoneData = create_kv(zoneData, "zi", zone.id)
	zoneData = create_kv(zoneData, "zx", zone.x)
	zoneData = create_kv(zoneData, "zy", zone.y)
	return "@".join(map(str, zoneData))