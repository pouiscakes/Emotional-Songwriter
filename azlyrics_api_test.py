import api.azapi
import time
from random import randint

def test():
	f = open('song_selection.txt', "r")
	# title = f.readline()
	# artist = f.readline()
	for line in f:
		line = line.split('-')
		artist = line[0]
		title = line[1]
	
		api.azapi.generating(artist, title, save=True)
		
		print artist
		print title

		time.sleep(randint(9, 11))
	f.close()
	
if __name__ == '__main__':
	test()

