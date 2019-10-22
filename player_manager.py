import time

import player

players = ["a", "b", "c"]

def update():
	updated = []
	for player in players:
		time.sleep(0.01)
		updated.append(player)
	print(updated)