import pandas as pd
import numpy as np

from gensim import corpora

df  = pd.read_csv('data_file/mecabChk_withoutJosa2.csv')

tokens = df['ORIGINAL']

rv_token = []

#nan 제거 
for token in tokens : 
	if pd.isna(token) : 
		pass
	else :
		word = token.split(' ')
		rv_token.append(word)

#make dictionary using review token  -> not a single string
dic = corpora.Dictionary(rv_token)
print(dic)


#doc2bow output -> (token_id, token_count),bow - bag of word  
#print(dic.doc2bow(rv_list))

# 출현빈도가 적거나 자주 등장하는 단어는 제거 
#dictionary.filter_extremes(no_below=10, no_above=0.05) 

#한 리뷰에 들어간 반복 단어 대한 카운트 
corpus = [dic.doc2bow(text) for text in rv_token]


#train lda modeling 

#전체리뷰를 가지고 토픽을 나눈 다음에 각 카페 리뷰를 토픽에 매핑하기..? 
import gensim 

NUM_TOPICS = 5

lda = gensim.models.ldamodel.LdaModel(corpus, num_topics = NUM_TOPICS, id2word=dic, passes =10)

topics = lda.print_topics(num_words = 5)
for topic in topics:
    print(topic)

#lda topic visualization 

import pyLDAvis
import pyLDAvis.gensim_models


vis = pyLDAvis.gensim_models.prepare(lda, corpus, dic)

pyLDAvis.save_html(vis,'lda_vis_origi.html')


#조사는 stopword로 빼고 다시 lda modeling 진행