import re
import pronouncing
from collections import defaultdict

word = "hair"
# rhymes = pronouncing.rhymes(word) 
# print rhymes 
phones = pronouncing.phones_for_word(word)[0]
phones_split = phones.split()
last_phone1 = phones_split[-1]

#try other ways instead of perfect rhyme
#1.synonyms, 2.near-rhymes (same kind of vowel), 3.match part of speech

d = defaultdict(int)

        

feeling = "joy"
with open("generated_lyrics_" + feeling + ".txt") as f:
	count = 0
	for line1 in f:
		line1 = line1.strip('\n')
		line1_split = line1.split() 
		last_word2 = line1_split[-1]
		last_word2 = re.sub("[^a-zA-Z]+", "", last_word2)

		phones2 = pronouncing.phones_for_word(last_word2)
		if phones2:
			phones2 = pronouncing.phones_for_word(last_word2)[0]
			phones_split2 = phones2.split()
			last_phone2 = phones_split2[-1]

			if last_phone2 == last_phone1:
				print (line1)
				count = count + 1
				d[last_word2] += 1
	print (count)
	print (last_phone1)
	print d
	print len(d)
		