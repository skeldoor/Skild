import time
import socket
import sys
from _thread import start_new_thread
import threading

import config

listOfConnections = []

s = None

def broadcast():
	global listOfConnections
	broadcasted = []
	for conn in listOfConnections:
		conn.sendall("data".encode())
		broadcasted.append(conn)
	print("Broadcasted to {} clients".format(len(broadcasted)))

def start_manager():
	global s
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socket.error as msg:
		print("Could not create socket. Error Code: ", str(msg[0]), "Error: ", msg[1])
		sys.exit(0)

	try:
		s.bind((config.HOST, config.PORT))
		print("[-] Socket Bound to port " + str(config.PORT))
	except socket.error as msg:
		print("Bind Failed. Error Code: {} Error: {}".format(str(msg[0]), msg[1]))
		sys.exit()

	s.listen(10)
	print("Listening...")
	t = threading.Thread(target=accept_loop)
	t.start()

def accept_loop():
	global listOfConnections
	while True:
		conn, addr = s.accept()
		print("[-] Connected to " + addr[0] + ":" + str(addr[1]))
		listOfConnections.append(conn)
		start_new_thread(client_thread, (conn,))
	sys.exit(0)

def client_thread(conn):
	conn.send("Welcome to the Server.\n".encode())
	while True:
		data = conn.recv(1024)
		if not data:
			break
		print(data)
		reply = "You sent: " + data.decode()
		conn.sendall(reply.encode())
	disconnect(conn)
	
def disconnect():
	global listOfConnections
	listOfConnections.remove(conn)
	conn.close()
	print("Conn closed")