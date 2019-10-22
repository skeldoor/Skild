import time

listOfConnections = [1,2,3]

def broadcast():
	broadcasted = []
	for connection in listOfConnections:
		time.sleep(0.01)
		broadcasted.append(connection)
	print(broadcasted)

def establish():
	pass

def disconnect():
	pass