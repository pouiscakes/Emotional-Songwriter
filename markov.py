'''
called by build_lyrics.php - generates lyrics in real-time
eventually should be prepared ahead of time
'''

import markovify

def generate_lyric(feeling, numberOfLines):
    with open("lyrics_" + feeling + ".txt") as f:
        text = f.read()

    # Build the model.
    text_model = markovify.NewlineText(text)

    with open("generated_lyrics_" + feeling + ".txt", "a+") as w:
        # Print i randomly-generated sentences
        for i in range(numberOfLines):
            lyric = text_model.make_short_sentence(50,tries=100) # 50 character count lines
            w.write(lyric + "\n")
            print(lyric)

def main():
    generate_lyric("joy", 10)

if __name__ == "__main__":
    main()