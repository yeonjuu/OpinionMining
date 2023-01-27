# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import TfidfVectorizer 
import pandas as pd


with open('offcoffee.txt') as f : 
	rv = f.read()

rv = [rv]
# text = ['I go to my home my home is very large', # Doc[0] 
#  		'I went out my home I go to the market', # Doc[1] 
#  		'I bought a yellow lemon I go back to home'] # Doc[2]


tfidf_vectorizer = TfidfVectorizer(ngram_range=(1,2), min_df = 1) # TF-IDF 객체선언
# max_features -> 길이 조절 
# vectorizer = TfidfVectorizer(max_features = 10)

tfidf_vectorizer.fit(rv) # 단어를 학습시킴 
tfidf_vectorizer.vocabulary_ # 단어사전을 출력 
#print(sorted(tfidf_vectorizer.vocabulary_.items())) # 단어사전 정렬, (vocabulary,idx)


x = tfidf_vectorizer.fit_transform(rv)
word=tfidf_vectorizer.get_feature_names()

from collections import defaultdict


word2id = defaultdict(lambda : 0)
for idx, feature in enumerate(word):
    word2id[feature] = idx


for i, sent in enumerate(rv):
	#print(x[i,word2id[token]] for token in sent.split(','))
    print([(token, x[i, word2id[token]]) for token in sent.split(',')])





# def sort_coo(coo_matrix):
# 	tuples = zip(coo_matrix.col,coo_matrix.data)
# 	return sorted(tuples, key=lambda x : (x[1], x[0]), reverse = True)

# def extract_topn_from_vector(feature_names,sorted_items,topn) : 
# 	sorted_items = sorted_items[:topn]
# 	score_vals = []
# 	feature_vals = []

# 	for idx , score in sorted_items : 
# 		score_vals.append(score)
# 		feature_vals.append(feature_names[idx])

# 	result={}
# 	for idx in range(len(feature_vals)) : 
# 		result[feature_vals[idx]] = score_vals[idx]

# 	return result

# import pandas as pd 

# df = pd.read_csv('data_file/MecabCheckedTotal.csv')

# from sklearn.feature_extraction.text import CountVectorizer 
# import re 

# # def get_stop_word(stop_file_path) :
# # 	with open(stop_file_path, 'r', encoding='utf-8') as f :
# # 		stopwords = f.readlines()
# # 		stop_set = set(m.strip() for m in stopwords)
# # 		return frozenset(stop_set)

# docs = df.MECAB

# cv = CountVectorizer(max_df=0.85)
# word_count_vector = cv.fit_transform(docs)

# list(cv.vocabulary_.keys())[:20]

# from sklearn.feature_extraction.text import TfidfTransformer 

# tfidf = TfidfTransformer(smooth_idf =True , use_idf=True)
# tfidf.fit(word_count_vector)

# feture_names = cv.get_feature_names()

# tfidf_vector = tfidf.transform(cv.transform(docs))

# sorted_items = sort_coo(tfidf_vector.tocoo())

# keywords= extract_topn_from_vector(feture_names,sorted_items,500)

# # print("-----DOC-----")
# # print(docs)
# print("-----Keywords-----")
# for k in keywords :
# 	print(k,keywords[k])


# #수학적으로 접근한 tf-idf 
# import pandas as pd 

# df = pd.read_csv('data_file/MecabCheckedTotal.csv')

# docs = df.MECAB[:100]

# vocab = list(set(w for doc in docs for w in doc.split(',')))
# vocab.sort()

# N = len(docs)

# def tf(t,d) : 
# 	return d.count(t)

# def idf(t) : 
# 	df = 0 
# 	for doc in docs:
# 		df += t in doc 
# 	return log(N/(df+1))

# def tfidf(t,d) : 
# 	return tf(t,d) + idf(t)

# result = []

# for i in range(N) : 
# 	result.append([])
# 	d = docs[i] 
# 	for j in range(len(vocab)) :
# 		t = vocab[j]
# 		result[-1].append(tf(t,d))

# tf_ = pd.DataFrame(result,columns = vocab)
# print(tf_)






