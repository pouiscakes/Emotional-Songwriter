'''
tool to print word count
'''

import operator
from collections import defaultdict

d = defaultdict(int)

def sort_to_dict(infile):
    for word in open(infile).read().split():
        d[word] += 1

def sorted_dict(infile):
    sort_to_dict(infile)
    return d

def vocabulary_count(infile):
    sort_to_dict(infile)
    return len(d)

def top_sorted_dict(infile, n):
    sort_to_dict(infile)
    return dict(sorted(d.iteritems(), key=operator.itemgetter(1), reverse=True)[:n])

def main():
    infile = 'generated_lyrics_joy.txt'

    print(sorted_dict(infile))
    print("VOCABULARY COUNT: " + str(vocabulary_count(infile)))
    print (top_sorted_dict(infile, 15))

if __name__ == '__main__':
    main()