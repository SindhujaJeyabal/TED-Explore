import pickle




class ted(object):

	def __init__(self):
		pass
	def dummy_function(self):
		print "I am a dummy"

# ***************************************************************
# tokenized by talk 
# ***************************************************************

	def words_talk(self):
		# list of talks, with list of words
		return pickle.load(open('../Corpus/words_talks.p', 'rb'))

	def word_sent(self):
		# list of talks with list of sentences, with list of words
		return pickle.load(open('../Corpus/sents_talks.p', 'rb'))

	def words_para(self):
		# list of talks, with list of paragraphs, with list of sentences, with list of words
		return pickle.load(open('../Corpus/words_paragraphs.p', 'rb'))

# ***************************************************************
# tokenized bag of entire corpus (not separated by talk)
# ***************************************************************


	def words_bag(self):
		# list of words
		return pickle.load(open('../Corpus/words_bag.p', 'rb'))

	def sents_bag(self):
		# list of sentences (as strings)
		return pickle.load(open('../Corpus/sents_bag.p', 'rb'))

# ***************************************************************
# tagged words
# ***************************************************************


	def tagged_words_talk(self):
		'''list of (str,str) tuple'''			# got it!
		return pickle.load(open('../Corpus/tagged_words_talks.p', 'rb'))		

	def tagged_sents_talk(self):
		'''list of (list of (str,str))'''		# got it!
		return pickle.load(open('../Corpus/tagged_sents_talks.p', 'rb'))

	def tagged_paras(self):
		'''list of (list of (list of (str,str)))'''
		return pickle.load(open('../Corpus/tagged_paragraphs.p', 'rb'))

	def tagged_topics(self):
		'''list of (list of (list of int, int, int, list of (str/str chunks))'''
		return pickle.load(open('../Corpus/tagged_topics.p', 'rb'))

# ***************************************************************
# 
# ***************************************************************


	def chunked_sents(self):
		'''list of (Tree with (str,str) leaves)'''

	def parsed_sents(self):
		'''list of (Tree with str leaves)'''

	def parsed_paras(self):
		'''list of (list of (Tree with str leaves))'''




class features(object):

	def __init__(self):
		pass

	def confusing(self):
		confusing_X = pickle.load('../Corpus/confusing.p', 'rb')
		# insert headers to y_labels because pandas DataFrames require headers
		confusing_y = pd.DataFrame(row[0] for row in y_labels().insert((0, "confusing", "funny", "informative")))
		return confusing_X, confusing_y

	def funny(self):
		funny_X = pickle.load('../Corpus/funny.p', 'rb')
		# insert headers to y_labels because pandas DataFrames require headers
		funny_y = pd.DataFrame(row[1] for row in y_labels().insert((0, "confusing", "funny", "informative")))
		return funny_X, funny_y

	def informative(self):
		informative_X = pickle.load('../Corpus/informative.p', 'rb')
		# insert headers to y_labels because pandas DataFrames require headers
		informative_y = pd.DataFrame(row[2] for row in y_labels().insert((0, "confusing", "funny", "informative")))
		return informative_X, informative_y

	def y_labels(self):
		'''list of tuples of category labels (confusing, funny, informative)
			[(20, 10, 2), ...n] where n = 177'''		# got it!
		return pickle.load(open('../Corpus/y.p', 'rb'))



