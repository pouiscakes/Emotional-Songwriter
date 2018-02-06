'''
no need to call this, it is imported in merge_lyrics.py
'''

def remove_duplicates(file_in, file_out):
    lines_seen = set() # holds lines already seen
    outfile = open(file_out, "w")
    for line in open(file_in, "r"):
        if line not in lines_seen: # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()