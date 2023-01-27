import pandas as pd
from hanspell import spell_checker
from hanspell.constants import CheckResult
import re 

file = pd.read_csv('./crawling/21.Byshankorea.csv')

rvs_serial = file['REVIEW']
rvs_serial.to_csv('reviews.txt', index=False, header=None, sep="\t")

f = open('reviews.txt','r',encoding='utf-8')
reviews = f.readlines()
#print(reviews)
f.close()
f2 = open('checked_byshan.txt','w',encoding='utf-8')
#문자 제거( 한글, 영어,숫자 제외)
pattern='([ㄱ-ㅎᄋᄑᄏᄒᄐㅏ-ㅣᅮ]+)'
repl=''

for i, document in enumerate(reviews):
    ##document = re.sub(r'[.,!?"\':;~()]', '', document)
    document = re.sub(r'[^ ㄱ-ㅣ가-힣A-Za-z0-9]', '', document) #특수기호 제거, 정규 표현식    
    #print(document) stale and uninspired
    reviews[i] = document
    try:
    	reviews[i] = re.sub(pattern=pattern, repl=repl, string=reviews[i])
    except: pass

for review in reviews : 
	#print(review)
	re_rv = spell_checker.check(review)
	check_rv = re_rv.checked
	f2.write(check_rv+"\n")

f2.close()

print("end")

