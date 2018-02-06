'''
called by build_lyrics.php - generates lyrics in real-time
eventually should be prepared ahead of time
'''

import markovify

def generate_lyric(feeling):
    with open("lyrics_" + feeling + ".txt") as f:
        text = f.read()

    # Build the model.
    text_model = markovify.NewlineText(text)

    with open("generated_lyrics_" + feeling + ".txt", "a+") as w:
        # Print i randomly-generated sentences
        for i in range(10):
            lyric = text_model.make_short_sentence(140,tries=100)
            w.write(lyric + "\n")
            print(lyric)

def main():
    generate_lyric("joy")

if __name__ == "__main__":
    main()