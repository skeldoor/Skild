import time

import config
import connection_manager as cm
import player_manager as pm

players = {}
npcs = {}

current_milli_time = lambda: int(round(time.time() * 1000))
last_milli_time = current_milli_time()

def main():
	running = True
	while running:
		serverLoop()

def serverLoop():
	process()
	publish()
	chill()

def process():
	pm.update()

def publish():
	cm.broadcast()

def chill():
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