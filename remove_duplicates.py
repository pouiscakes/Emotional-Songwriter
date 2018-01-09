lines_seen = set() # holds lines already seen
outfile = open("merged_lyrics_unique.txt", "w")
for line in open("merged_lyrics_clean.txt", "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()