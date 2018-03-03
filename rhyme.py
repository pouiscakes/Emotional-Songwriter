import re
import pronouncing
from collections import defaultdict


def ending_word(line):
    # get the ending word of each line
    line_split = line.split() 
    last_word = line_split[-1] 
    last_word = re.sub("[^a-zA-Z]+", "", last_word) 
    return last_word

def last_phone(line):
    last_word = ending_word(line)

    # get the ending phoneme of the word
    phones = pronouncing.phones_for_word(last_word)
    if phones:
        phones = phones[0]
        phones_split = phones.split()
        last_phone = phones_split[-1]
        return last_phone
    else:
        return 0


		
def rhyme(feeling):
    # word = "hair"
    # phones = pronouncing.phones_for_word(word)[0]
    # phones_split = phones.split()
    # last_phone1 = phones_split[-1]

    #try other ways instead of perfect rhyme
    #1.synonyms, 2.near-rhymes (same kind of vowel), 3.match part of speech

    # vocabulary = defaultdict(int)
    with open("rhymed_lyrics_" + feeling + ".txt", 'w+') as w:
        with open("generated_lyrics_" + feeling + ".txt") as f1:
            # count = 0
            line1_index = 0
            for line1 in f1:
                line1 = line1.strip('\n')
                last_phone1 = last_phone(line1)
                line1_index += 1
                line2_index = 0

                with open("generated_lyrics_" + feeling + ".txt") as f2:
                    for line2 in f2:
                        # skip previously compared lines
                        if line2_index < line1_index:
                            line2_index += 1     

                        else:
                            line2 = line2.strip('\n')
                            last_phone2 = last_phone(line2)

                            if last_phone2 == last_phone1 and ending_word(line1) != ending_word(line2):
                                print (line1)
                                print (line2)
                                print " "
                                w.write(line1 + "\n" + line2 + "\n\n")
                                break
                                # count = count + 1
                                # vocabulary[last_word2] += 1
            # print (count)
            # print (last_phone1)
            # print vocabulary
            # print len(vocabulary)

if __name__ == "__main__":
    rhyme("joy")