import glob


read_files = glob.glob("song_lyrics_raw/*.txt")

with open("merged_lyrics.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
        outfile.write("\n")

import clean_bad_words
import remove_duplicates