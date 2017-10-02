import api.azapi

def test():
	artist = "mark ronson"
	title = "uptown funk"
	
	api.azapi.generating(artist, title, save=True)
	
	
if __name__ == '__main__':
	test()

