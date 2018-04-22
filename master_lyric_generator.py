import merge_lyrics
import emotion
import markov
import rhyme
import vocabulary_count

merge_lyrics.merge()
emotion.sort()

# feelings = {"joy", "sadness", "anger", "fear", "surprise"}
feelings = {"joy"} # only joy for the kids

for feeling in feelings:
    # generate in increments of 1000, then 100 until vocabulary stops increasing
    # or just 3200
    markov.generate_lyric(feeling, 3200) 
    print("VOCABULARY COUNT: " + str(vocabulary_count.vocabulary_count("generated_lyrics_" + feeling + ".txt")))

    rhyme.rhyme(feeling)