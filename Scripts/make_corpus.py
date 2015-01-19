import nltk
import pickle


text = []
with open('ted.txt') as f:
	for line in f:
		text.append(line)

#sent_tokenized = [nltk.sent_tokenize(talk) for talk in text]	# []
#word_tokenized = [nltk.word_tokenize(sent) for sent in sent_tokenized]
#pickle.dump(word_tokenized, open( "words.p", "wb" ))
#tagged = nltk.pos_tag(word for word in word_tokenized)

print text[282]