import random

# List of words
nouns = ["cat", "dog", "elephant", "tree", "mountain"]
verbs = ["runs", "jumps", "sleeps", "eats", "climbs"]
adjectives = ["happy", "green", "tall", "angry", "soft"]
adverbs = ["quickly", "silently", "loudly", "slowly", "carefully"]

# Generate a random sentence
random_noun = random.choice(nouns)
random_verb = random.choice(verbs)
random_adjective = random.choice(adjectives)
random_adverb = random.choice(adverbs)

sentence = f"The {random_adjective} {random_noun} {random_verb} {random_adverb}."

print(sentence)
crazy_sentence_generator.py
