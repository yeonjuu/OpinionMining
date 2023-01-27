import knuMd
import pandas as pd

onoffdf = pd.read_csv('data_file/OnOffList.csv',encoding='CP949')
df = pd.read_csv('data_file/MecabCheckedTotal.csv')

mecab = df['MECAB']

foods = onoffdf['음식']
places = onoffdf['공간']
services = onoffdf['가격서비스']

dic = ['food','place','csNprice']

knu = knuMd.KnuSL

on = 0

food_scores=[] ; place_scores = [] ; service_scores = []
food_cnts = [] ; place_cnts = [] ; service_cnts = []

f_score = 0; p_score = 0; s_score = 0
f_cnt =0; p_cnt = 0 ; s_cnt = 0;

for i in range(len(mecab)) :
	if i%500 == 0 : 
		print('ing')
	words = mecab[i].split(',')
	#print(mecab[i])
	for word in words :
		for food in foods : 
			if word == food :
				on = 1  
		for place in places : 
			if word == place :
				on = 2 
		for service in services : 
			if word == service : 
				on = 3

		if on == 1 : 
			score , cnt = knu.data_list(word)
			if score != 'None' : 
				f_score += int(score)
			if cnt != 0 : 
				f_cnt += int(cnt)
			#print(dic[on-1],f_score,f_cnt)

		elif on == 2 : 
			score , cnt = knu.data_list(word)
			if score != 'None' : 
				p_score += int(score)
			if cnt != 0 : 
				p_cnt += int(cnt)
			#print(dic[on-1],p_score,p_cnt)

		elif on == 3 : 
			score , cnt = knu.data_list(word)
			if score != 'None' : 
				s_score += int(score)
			if cnt != 0 : 
				s_cnt += int(cnt)
			#print(dic[on-1],s_score,s_cnt)

	on = 0

	food_scores.append(f_score)
	place_scores.append(p_score)
	service_scores.append(s_score)

	food_cnts.append(f_cnt)
	place_cnts.append(p_cnt)
	service_cnts.append(s_cnt) 

	f_score = 0 ; p_score = 0; s_score = 0
	f_cnt = 0 ; p_cnt=0; s_cnt=0

print('csv convert')

#print('SENTIMENT ','food : ',food_scores,' place : ',place_scores,' csNprice : ',service_scores)
#print('COUNT ','food : ',food_cnts,' place : ',place_cnts,' csNprice : ',service_cnts)

cate_list = [] 

for i in zip(mecab, food_scores, food_cnts , place_scores, place_cnts,service_scores,service_cnts) : 
	cate_list.append(
		[
			i[0],
			i[1],
			i[2],
			i[3],
			i[4],
			i[5],
			i[6],
		]
	)


cate_infos = pd.DataFrame(cate_list, columns = ['REVIEW','FOOD','COUNT1','PLACE','COUNT2','SERVICE','COUNT3'])
cate_infos.to_csv('Category_Info.csv',index=False, encoding = 'utf-8-sig')

noCate = 0

for i in zip(food_cnts,place_cnts,service_cnts) : 
	if i[0] == 0 and i[1] ==0 and i[2] == 0 :
		noCate += 1 


print(noCate)
print(noCate/len(mecab))
