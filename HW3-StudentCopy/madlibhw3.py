print("START*******")

import nltk 
from nltk.book import *
import random
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import gutenberg


# Using text2 from the nltk book corpa, create your own version of the


# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text

tagged_tokens = nltk.pos_tag(text2) 
tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective", "RB": "an adverb"}
substitution_probabilities = {"NN":.15,"NNS":.15,"VB":.1,"JJ":.1, "RB":.1}

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

orig = []
s = tagged_tokens[:150]
for tup in s:
	orig.append(tup[0])

final_words = []

print('ORIGINAL TEXT')
print(" ".join(orig))

for (word, tag) in tagged_tokens[:150]:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))

print ("".join(final_words))



print("\n\nEND*******")
