from nltk.corpus import wordnet as wn

word = 'green'
print '\n\n'
print '========== ' + word.upper() + ' ==========='
synsets = wn.synsets(word)
print synsets

# synsets = [Synset('pretty.s.01'), Synset('pretty.s.02'), Synset('reasonably.r.01')]
for synset in synsets:
	print '----------------------------- ' + synset.definition()
# synset = wn.synset('dog.n.01')
	print '--------------- Hypernyms'
	for hypernym in synset.hypernyms():
		print hypernym.lemmas()[0].name()
	print '--------------- Hyponyms'
	for hyponym in synset.hyponyms():
		print hyponym.lemmas()[0].name()
	# for lemma in synset.lemmas():
	# 	print lemma.name()
# print(synsets[0].definition())

