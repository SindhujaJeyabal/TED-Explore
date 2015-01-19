import json, urllib, csv
import nltk

def get_text(jobject, urls):
	texts = []
	for talk in jobject['results']:
		if talk['url'] not in urls:
			#print talk['url']
			text = []
			for line in talk['content']:
				text.append(line['words']['text'].encode('ascii', 'ignore'))
			blob = ' '.join(text)
			texts.append(blob)
			urls.append(talk['url'])
	return texts, urls

def get_metadata(jobject):
	meta = []
	for talk in jobject['results']['collection1']:
		meta.append((talk['title'].encode('ascii', 'ignore'), 
			talk['speaker'].encode('ascii', 'ignore')[:-1], 
			talk['nviews'].encode('ascii', 'ignore'), 
			talk['topics'].encode('ascii', 'ignore')))
	return meta

# ***************************************
# Create Transcript File (of speakers' words)
# ***************************************

amount = 0 
#total = 52113
api_call = "https://www.kimonolabs.com/api/92nwvy72?apikey=VP6IONzhcPRy5y0C3OVQ6o07Kp85v6vC&kimbypage=1&kimoffset="
total_list = []
urls = []

while amount <= 50000:
	texts, urls = get_text(json.load(urllib.urlopen(api_call+str(amount))), urls)
	total_list.extend(texts)
	amount += 2500

print "Created a list of talks!"
print "Length = %d" %len(total_list)	# len of total_list is 177

sent_tokenized = [nltk.sent_tokenize(talk) for talk in total_list]	# [ [sent1, sent2], [talk2] ]
print "Sentences are tokenized!"	

word_tokenized = [nltk.word_tokenize(sent) for sent in sent_tokenized]	# [ [ [word1, word2], [sent2] ], [talk2] ]: list of talks that are a list of sents that are a list of words
print "Words are tokenized! Pickling words..."
pickle.dump(word_tokenized, open( "words_talks.p", "wb" ))
print word_tokenized[0]

print "POS tagging. This may take a while..."
tagged = [nltk.pos_tag(sent) for sent in talk for talk in word_tokenized]
pickle.dump(tagged, open("tagged_talks.p", "wb"))

text_as_one_string = ' '.join(total_list)
bag_sent_tokens = [nltk.sent_tokenize(text_as_one_string)]
bag_word_tokens = [nltk.word_tokenize(sent) for sent in bag_sent_tokens]
pickle.dump(bag_word_tokens, open("bag_words.p", "wb"))

"""
filepath = '/Users/matthewvalente/Documents/ischool/fall14/Info256_NLP/ted/'
transcript_file = 'ted.txt'
with open(filepath+transcript_file, 'w') as f:
	f.writelines(total_list)
"""


# ***************************************
# Create Metadata File: CSV of [title, speaker, nviews, topics]
# ***************************************
"""
meta_api = "https://www.kimonolabs.com/api/d9qrkfyg?apikey=VP6IONzhcPRy5y0C3OVQ6o07Kp85v6vC"

metadata = get_metadata(json.load(urllib.urlopen(meta_api)))

metadata_file = 'meta.txt'
metadata.insert(0, ('title', 'speaker', 'nviews', 'topics'))

meta_csv = 'meta.csv'

with open(filepath+meta_csv, 'wb') as csv_file:
	writer = csv.writer(csv_file, delimiter=',')
	for line in metadata:
		writer.writerow(line)
"""