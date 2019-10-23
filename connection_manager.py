import time
import socket
import sys
from _thread import start_new_thread
import threading

import config
import player_manager
from player import Player

class Connection_manager(object):

	def __init__(self):
		self.s = None

	def broadcast(self, pm):
		broadcasted = []
		for player in pm.listPlayers():
			try:
				player.connection.sendall("data".encode())
				broadcasted.append(player)
			except socket.error as msg:
				pm.remove(player)
		# print("Broadcasted to {} clients".format(len(broadcasted)))

	def start_manager(self):
		try:
			self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		except socket.error as msg:
			print("Could not create socket. Error Code: ", str(msg[0]), "Error: ", msg[1])
			sys.exit(0)

		try:
			self.s.bind((config.HOST, config.PORT))
			print("[-] Socket Bound to port " + str(config.PORT))
		except socket.error as msg:
			print("Bind Failed. Error Code: {} Error: {}".format(str(msg[0]), msg[1]))
			sys.exit()

		self.s.listen(10)
		print("Listening...")

	def accept_loop(self, pm):
		while True:
			conn, addr = self.s.accept()
			print("[-] Connected to " + addr[0] + ":" + str(addr[1]))
			start_new_thread(self.client_thread, (conn, pm))
		sys.exit(0)

	def client_thread(self, conn, pm):
		conn.send("Welcome to the Server.\n".encode())
		player = Player(25, 25, 1, 1, None, (255, 0, 255), "Player 1", 1, 1, conn)
		pm.add(player)
		while True:
			data = conn.recv(1024)
			if not data:
				break
			print(data)
			reply = "You sent: " + data.decode()
			conn.sendall(reply.encode())
		self.disconnect(conn)
		
	def disconnect(self, conn):
		conn.close()
		print("Conn closed")