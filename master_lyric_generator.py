import markov
import rhyme
import vocabulary_count

feeling = "joy"
feelings = {"sadness", "anger", "fear", "surprise"}
for feeling in feelings:

    # generate in increments of 1000, then 100 until vocabulary stops increasing
    markov.generate_lyric(feeling, 3200) 
    print("VOCABULARY COUNT: " + str(vocabulary_count.vocabulary_count("generated_lyrics_" + feeling + ".txt")))

    rhyme.rhyme(feeling)