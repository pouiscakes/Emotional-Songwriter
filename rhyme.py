import re
import pronouncing
from collections import defaultdict


def ending_word(line):
    # get the ending word of each line
    line_split = line.split() 
    last_word = line_split[-1] 
    last_word = re.sub("[^a-zA-Z]+", "", last_word) 
    return last_word

def last_phones(line, num_phones):
    last_word = ending_word(line)

    # get the ending phoneme of the word
    phones = pronouncing.phones_for_word(last_word)
    if phones:
        phones = phones[0]
        phones_split = phones.split()
        result_phones = []
        if len(phones_split) >= num_phones:
            for i in range(1, num_phones + 1):
                result_phones.append(phones_split[-i])
        else:
            result_phones.append(phones_split[-1])
        return result_phones
    else:
        return 0

def last_vowel_phones(line, num_phones):
    last_word = ending_word(line)
    vowels = {'AA1', 'AE1', 'AH1', 'AO1', 'AW1', 'AY1', 'EH1', 'ER1', 'EY1', 'IH1', 'IY1', 'OW1', 'OY1', 'UH1', 'UW1', 'AA0', 'AE0', 'AH0', 'AO0', 'AW0', 'AY0', 'EH0', 'ER0', 'EY0', 'IH0', 'IY0', 'OW0', 'OY0', 'UH0', 'UW0'}

    # get the ending phoneme of the word
    phones = pronouncing.phones_for_word(last_word)
    if phones:
        phones = phones[0]
        phones_split = phones.split()
        result_phones = []
        vowel_phones = []
        for phone in phones_split:
            # print (phone)
            if phone in vowels:
                vowel_phones.append(phone)
                
        if len(vowel_phones) >= num_phones:
            for i in range(1, num_phones + 1):
                result_phones.append(vowel_phones[-i])
        else:
            result_phones.append(vowel_phones[-1])
            return 0
        return result_phones
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
                last_phone1 = last_phones(line1, 2)
                last_vowel_phones1 = last_vowel_phones(line1, 2)
                line1_index += 1
                line2_index = 0

                with open("generated_lyrics_" + feeling + ".txt") as f2:
                    for line2 in f2:
                        # skip previously compared lines
                        if line2_index < line1_index:
                            line2_index += 1     

                        else:
                            line2 = line2.strip('\n')
                            last_phone2 = last_phones(line2, 2)
                            last_vowel_phones2 = last_vowel_phones(line2, 2)

                            # match exact rhymes - last two phones
                            if last_phone2 == last_phone1 and last_phone1 != 0 and ending_word(line1) != ending_word(line2):
                                print(last_phones(line1, 2))                           
                                print (line1)
                                print (line2)
                                print " "
                                w.write(line1 + "\n" + line2 + "\n\n")
                                break

                            # match near rhymes - last two vowel phones 
                            elif last_vowel_phones2 == last_vowel_phones1 and last_vowel_phones1 != 0 and ending_word(line1) != ending_word(line2):
                                print(last_vowel_phones(line1, 2))                           
                                print (line1)
                                print (line2)
                                print " "
                                w.write(line1 + "\n" + line2 + "\n\n")
                                break
                            
                            

                                
            # print (count)
            # print (last_phone1)
            # print vocabulary
            # print len(vocabulary)

if __name__ == "__main__":
    rhyme("joy")