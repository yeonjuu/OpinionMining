import pandas as pd 
import CatSenti 


df = pd.read_csv('data_file/MecabCheckedTotal.csv')

mecab = df['MECAB']

catsenti = CatSenti.CatSenti 

cum_scores =[]
cum_score = 0

word_cnts = []
word_cnt = 0

for i in range(0,len(mecab)) :
	words = mecab[i].split(',')
	for word in words :
		score,cnt = catsenti.data_list(word)
		if score != 'None' : 
			cum_score += int(score)
		if cnt != 0 : 
			word_cnt += int(cnt)
	if i%500 == 0 : 
		print(i," 번째 리뷰점수 : ",cum_score)


	cum_scores.append(cum_score)
	cum_score = 0;
	word_cnts.append(word_cnt)
	word_cnt = 0 
	#print("SENT : ",cum_scores[i],'WORD : ', word_cnts[i])


print('end')

user = df['USER']

rv_list = []

for item in zip(user,mecab,cum_scores, word_cnts) : 
	rv_list.append(
		[
			item[0],
			item[1],
			item[2],
			item[3],
		]
	) 

rv_infos = pd.DataFrame(rv_list, columns = ['USER','REVIEW','SENTI','COUNT'])
rv_infos.to_csv('PriceService.csv',index=False, encoding = 'utf-8-sig')


