import knusl
import pandas as pd
import csv 

#none_okt = []
none_list = []

#file_list = ['12.Onion','13.Twosome','14.CenterCoffee','15.Humbolt','16.DaelimCG']
#file_list=['17.Granpafactory','18.Zagmachi','19.Ongkeundal','20.Scene','21.Byshankorea']
rv= pd.read_csv('data_file/LALA_Mecab.csv')
	#rvs_okt = rv['OKT']

mecab = rv['MECAB']
	#file = open('16.okt.DaelimCG.txt','r', encoding='utf-8')

knu = knusl.KnuSL

cum_scores =[]
cum_score = 0

	# print('------------okt------------')

	# #review 한 문장을 단어로 분리해서 리스트에 저장 
	# for i in range(len(rvs_okt)) :
	# 	if pd.isna(rvs_okt[i]) :
	# 		arr = "."
	# 	else:	
	# 		arr = rvs_okt[i].split(',')
	# 	#한 단어씩 감성점수 부여
	# 	for j in range(len(arr)) : 
	# 		word = arr[j]
	# 		x,score = knu.data_list(word)
	# 		if  score != 'None' :	
	# 			cum_score += int(score)
	# 		else:
	# 			none_okt.append(word)

	# 	print(i," 번째 리뷰점수 : ",cum_score)
	# 	cum_scores.append(cum_score)
	# 	#reset cum_score
	# 	cum_score = 0;

	# print(cum_scores)
	
print('------------MECAB------------')

for i in range(0,len(mecab)) :
	if pd.isna(mecab[i]) :
		arr = "."
	else:	
		arr = mecab[i].split(',')
	#한 단어씩 감성점수 부여
	for j in range(len(arr)) : 
		word = arr[j]
		x,score = knu.data_list(word)
		if  score != 'None' :	
			cum_score += int(score)
		else:
			none_list.append(word)
	if i%500 ==0 :
		print(i," 번째 리뷰점수 : ",cum_score)

	cum_scores.append(cum_score)
	cum_score = 0;
		#reset cum_score

# mecab_list = {'mecab_none_word' : none_list}

# # okt_df = pd.DataFrame(okt_list)
# # okt_df.to_csv('okt_list_17To21.csv',header='false',index='false',encoding='utf-8-sig')

# Mecab_df = pd.DataFrame(mecab_list)
# Mecab_df.to_csv('None_list_01.csv',header='false',index='false',encoding='utf-8-sig')

# users = rv['USER'][4500:]
# scores = rv['SCORE'][4500:]
# reviews = rv['ORIGINAL'][4500:]

#mecab = rv['MECAB']

user = rv['USER']
score = rv['SCORE']
orig = rv['ORIGINAL']


rv_list=[]

for item in zip(user,score,orig,mecab,cum_scores) : 
	rv_list.append(
		[ 
			item[0],
			item[1],
			item[2],
			item[3],
			item[4],
		]
	)

rv_infos = pd.DataFrame(rv_list, columns =['USER','SCORE','ORIGINAL','MECAB','SENT_SCORE'])
rv_infos.to_csv('Test_LALA.csv', index =False,encoding = 'utf-8-sig')
#okt_list = { 'Okt_none_word' : none_okt}


#비싸지만 맛있어요  구경거리도 많고 노래도 좋고 좋았습니다 
#[('비싸다', 'Adjective'), ('맛있다', 'Adjective'), ('구', 'Modifier'), ('경', 'Modifier'), ('거리', 'Noun'), ('도', 'Josa'), ('많다', 'Adjective'), ('노래', 'Noun'), ('도', 'Josa'), ('좋다', 'Adjective'), ('좋다', 'Adjective')]
# arr = ['비싸다','맛있다','구','경','거리','도','많다','노래','도','좋다','좋다']

# cum_score = 0 ;


# for i in range(0,len(arr)) : 
# 	word = arr[i]
# 	x, score = knu.data_list(word)
# 	if score == 'None' :
# 		pass
# 	elif score != 'None' : 
# 		cum_score += int(score)

# print(arr," , 리뷰점수 : ",cum_score)