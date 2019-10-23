import time
import threading

import config
from connection_manager import Connection_manager
from player_manager import Player_manager

players = {}
npcs = {}

current_milli_time = lambda: int(round(time.time() * 1000))
last_milli_time = current_milli_time()

running = None

def main():
	global running
	running = True
	cm = Connection_manager()
	cm.start_manager()
	pm = Player_manager()
	accept_thread = threading.Thread(target=cm.accept_loop, args=(pm,))
	accept_thread.start()
	t = threading.Thread(target=serverLoop, args=(cm, pm))
	t.start()
	
def serverLoop(cm, pm):
	while running:
		process(pm)
		publish(cm, pm)
		chill()

def process(pm):
	# print("Processing...")
	pm.update()

def publish(cm, pm):
	cm.broadcast(pm)

def chill():
	# print("Chilling...\n")
	global running
	global last_milli_time
	timeSpentProcessing = current_milli_time() - last_milli_time
	timeToSleep = (config.SERVER_TICK_RATE_MILLIS - timeSpentProcessing) / 1000
	if timeToSleep < 0:
		config.LOG.warning("Processing took too long at %sms", str(timeSpentProcessing))
		timeToSleep = 0
	time.sleep(timeToSleep)
	last_milli_time = current_milli_time()

if __name__ == "__main__":
	main()
	