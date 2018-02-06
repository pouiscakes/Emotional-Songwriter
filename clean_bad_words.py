'''
no need to call this, it is imported in merge_lyrics.py
'''

def clean_bad_words(in_file, out_file):
    with open('bad_words.txt') as f:
        bad_words = f.readlines() # convert text file to array
    bad_words = [x.strip() for x in bad_words] # remove whitespace

    with open(in_file) as oldfile, open(out_file, 'w') as newfile:
        for line in oldfile:
            if not any(bad_word in line for bad_word in bad_words):
                newfile.write(line)