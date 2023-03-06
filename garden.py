import spacy

nlp = spacy.load("en_core_web_sm")

gardenpathSentences = [
    "The complex houses married and single soldiers and their families.",
    "The horse raced past the barn fell.",
    "The girl told the story cried.",
    "I convinced her children are noisy.",
    "She told me a little white lie will come back to haunt me.",
]

for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print(f"\nSentence: {sentence}\n")
    print([(w.text, w.pos_) for w in doc])


print(spacy.explain("DET"))
print(spacy.explain("CCONJ"))


# What was the entity and its explanation that you looked up?
# DET = Determiner
# CCONJ = Coordinating Conjunction

# Did the entity make sense in terms of the word associated with it?
# Yes
