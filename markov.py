import markovify

# Get raw text as string.
with open("lyrics_joy.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.NewlineText(text)

# Print five randomly-generated sentences
for i in range(3):
    print(text_model.make_short_sentence(140,tries=100))