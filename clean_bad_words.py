# bad_words = ['bad', 'naughty']
with open('bad_words.txt') as f:
    bad_words = f.readlines() # convert text file to array
bad_words = [x.strip() for x in bad_words] # remove whitespace

with open('merged_lyrics.txt') as oldfile, open('merged_lyrics_clean.txt', 'w') as newfile:
    for line in oldfile:
        if not any(bad_word in line for bad_word in bad_words):
            newfile.write(line)