import time
import threading
import google

import config
from connection_manager import Connection_manager
from player_manager import Player_manager
from game_manager import Game_manager
import Keyframe_pb2


players = {}
npcs = {}

current_milli_time = lambda: int(round(time.time() * 1000))
last_milli_time = current_milli_time()

running = None

def main():
	global running
	running = True
	init()

def init():
	keyFrame = Keyframe_pb2

	keyFrame.KEYFRAME.YOUDATA.playerID = 123
	print(keyFrame.KEYFRAME.YOUDATA.playerID)

	quit()

	gm = Game_manager()
	cm = Connection_manager()
	cm.start_manager()
	pm = Player_manager()
	accept_thread = threading.Thread(target=cm.accept_loop, args=(pm, gm))
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
	