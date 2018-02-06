# import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
# import matplotlib.pyplot as plt
import indicoio
import operator

indicoio.config.api_key = 'a816b53c9820893345ae9fe2570d5fb8'

def sort():
	with open("merged_lyrics_unique.txt", "r") as f:
		for line in f:
			if not line.isspace(): 
				emotion =  indicoio.emotion(line)

				song = line
				print song

				anger = emotion.get('anger')
				surprise = emotion.get('surprise')
				sadness = emotion.get('sadness')
				fear = emotion.get('fear')
				joy = emotion.get('joy')

				print "anger: " + str(anger)
				print "surprise: " + str(surprise)
				print "sadness: " + str(sadness)
				print "fear: " + str(fear)
				print "joy: " + str(joy)

				result = str(max(emotion.iteritems(), key=operator.itemgetter(1))[0])

				print "result: " + result

				with open("lyrics_" + result + ".txt", "a") as outfile:
					outfile.write(line)

if __name__ == "__main__":
    sort()

# objects = ('anger', 'surprise', 'sadness', 'fear', 'joy')
# y_pos = np.arange(len(objects))
# performance = [anger, surprise, sadness, fear, joy]
 
# plt.bar(y_pos, performance, align='center', alpha=0.5)
# plt.xticks(y_pos, objects)
# plt.ylabel('Probability')
# plt.title('Emotion Analysis of ' + song)
 
# plt.show()


# print "done"

# # batch example
# indicoio.emotion([
#     "I did it. I got into Grad School. Not just any program, but a GREAT program. :-)",
#     "Like seriously my life is bleak, I have been unemployed for almost a year."
# ])
