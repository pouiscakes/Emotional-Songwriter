import api.azapi

def test():
	f = open('song_selection.txt', "r")
	# title = f.readline()
	# artist = f.readline()
	line = f.readline().split('-')
	artist = line[0];
	title = line[1];
	f.close()
	
	api.azapi.generating(artist, title, save=True)
	
	print artist
	print title
	
if __name__ == '__main__':
	test()

