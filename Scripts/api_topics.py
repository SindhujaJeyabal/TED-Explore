import nltk, re, pickle
from nltk.corpus import stopwords
print "Text Tiling.. This takes a while..."
tagged_paras = pickle.load(open('../Corpus/tagged_paragraphs.p', 'rb'))
tt = nltk.tokenize.texttiling.TextTilingTokenizer()
bounds_list = list()
for talk in tagged_paras:
    para_list = list()
    w_count = 0
    for para in talk:
        sent_list = list()        
        for sent in para:
            sent_list.append(' '.join([word+"/"+tag for word,tag in sent if word not in stopwords.words('english')]))
            w_count += len(sent)
        para_list.append(' '.join(sent_list))   
    talk_text = '\n\n\t'.join(para_list)
    if len(para_list) < 2:
        bounds_list.append((len(para_list),0, w_count, talk_text))
        continue
    
    b_text = tt.tokenize(talk_text)
    print len(b_text)
    bounds_list.append((len(para_list), len(b_text), w_count, b_text))
print bounds_list[0]
pickle.dump(bounds_list, open("../Corpus/tagged_topics.p", "wb"))