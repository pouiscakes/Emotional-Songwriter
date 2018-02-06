'''
use this to prepare lyrics. 
'''

import glob
import remove_duplicates
import clean_bad_words

def merge():
    read_files = glob.glob("song_lyrics_raw/*.txt")

    with open("merged_lyrics.txt", "wb") as outfile:
        for f in read_files:
            with open(f, "rb") as infile:
                outfile.write(infile.read())
            outfile.write("\n")
            
    clean_bad_words.clean_bad_words("merged_lyrics.txt", "merged_lyrics_clean.txt")
    remove_duplicates.remove_duplicates("merged_lyrics_clean.txt", "merged_lyrics_unique.txt")

if __name__ == "__main__":
    merge()