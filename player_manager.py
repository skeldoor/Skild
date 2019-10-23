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
		#print(updated)

	def add(self, player):
		self.players.append(player)
		# config.LOG.info("Player %s joined the game", str(player.name))
		print("Player ", str(player.name), " joined the game")

	def remove(self, player):
		self.players.remove(player)
		# config.LOG.info("Player %s left the game", str(player.name))
		print("Player ", str(player.name), " left the game")

	def listPlayers(self):
		return self.players