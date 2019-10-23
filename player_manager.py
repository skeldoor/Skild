import time

import player
import config

class Player_manager(object):

	def __init__(self):
		self.players = []

	def update(self):
		updated = []
		for player in self.players:
			player.update()
			updated.append(player)
		print(updated)

	def add(self, player):
		self.players.append(player)
		config.LOG.warning("Player %s joined the game", str(player.name))

	def remove(self, player):
		self.players.remove(players)
		config.LOG.warning("Player %s left the game", str(player.name))

	def listPlayers(self):
		return self.players