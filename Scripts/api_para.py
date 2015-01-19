import json, urllib, csv
import nltk, re, pickle

def get_text(jobject, urls):
	texts = []
	for talk in jobject['results']:
		if talk['url'] not in urls:
			text = []
			for paragraph in talk['collection1']:
				try:													# some paragraphs contain other objects that we don't want
					p = paragraph['paragraph'].encode('ascii', 'ignore')
					index = re.search(r"\d+:\d+", p).end()		# find position of sentence beginning "18:32\nWhat TED celebrates..."
					text.append(p[index:])
				except:
					pass
			texts.append(text)
			urls.append(talk['url'])
	return texts, urls

# json object 
#{"results" : 
#	{ 	"url": "www.ted.com/talks/ken...",	
#		"page" : "1",	
#		"collection1": 
#			"paragraph" : [ 
#				"0:11\nHow now brown cow..."},
#				"1:23\nPurple monkey dishwasher..." ]

api_call = "https://www.kimonolabs.com/api/5m2wqe68?apikey=VP6IONzhcPRy5y0C3OVQ6o07Kp85v6vC&kimbypage=1&kimoffset="


amount = 0
talks = []
urls = []

while amount <= 5000:		# total rows is 5,318 so there will be 3 api calls
	texts, urls = get_text(json.load(urllib.urlopen(api_call+str(amount))), urls)
	talks.extend(texts)
	amount += 2500

pickle.dump(talks, open("../Corpus/talks_paragraphs.p", "wb"))
print talks[0]
print ("Number of talks: %d" % len(talks))

sent_tokenized = [[nltk.sent_tokenize(paragraph) for paragraph in talk] for talk in talks]	
print "Sentences are tokenized!"	
#[talks
#	[talk
#		[paragraph
#			[sentence  
#				[words] ] ] ] ] 

word_tokenized = [[[nltk.word_tokenize(sent) for sent in paragraph] for paragraph in talk] for talk in sent_tokenized]
print "Words are tokenized! Pickling words..."
pickle.dump(word_tokenized, open( "../Corpus/words_paragraphs.p", "wb" ))
print word_tokenized[0]

print "POS tagging. This may take a while..."
tagged = [[[nltk.pos_tag(sent) for sent in paragraph] for paragraph in talk] for talk in word_tokenized]
pickle.dump(tagged, open("../Corpus/tagged_paragraphs.p", "wb"))
print "Done POS tagging!"
print tagged[0]

