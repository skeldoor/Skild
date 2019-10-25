import Keyframe_pb2

def parse_incoming(data):
	print(data)

def format_outgoing(blob):
	print(blob)

def format_keyframe(player, pm, gm):
	input = []

	keyFrame = Keyframe_pb2.KEYFRAME()

	youData.playerID = 123
	youData.playerx = player.xposition
	youData.playery = player.yposition
	youData.playerColour = "yellow"

	# playerList = pm.listPlayers()
	# try:
	# 	playerList = playerList.remove(player)
	# except:
	# 	pass

	# count = 0
	# for otherPlayer in playerList:
	# 	playerData = keyFrame.PLAYERDATA.add()
	# 	playerData.playerID = count
	# 	playerData.playerX = otherPlayer.xposition
	# 	playerData.playerY = otherPlayer.yposition
	# 	count = count + 1

	print("keyframe is: " + str(keyFrame))
	return keyFrame.SerializeToString()

def serialise_map_data(gm):
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