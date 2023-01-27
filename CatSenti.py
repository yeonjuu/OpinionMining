import json


class CatSenti():
 
	# def data_list(wordname):
	# 	dic = ['food_info','place_info','csNprice_info']	
	# 	with open('data/food_info.json', encoding='utf-8-sig', mode='r') as f:
	# 		data = json.load(f)
	# 	result = ['None']	
	# 	w_cnt = 0
	# 	for i in range(0, len(data)):
	# 		if data[i]['word'] == wordname:
	# 			result.pop()
	# 			result.append(data[i]['polarity'])	
	# 			w_cnt += 1 

	# 	s_word = result[0]

	# 	return s_word, w_cnt 

	def data_list(wordname,dic_num):
		dic = ['food_info','place_info','csNprice_info']
		with open('data/'+dic[dic_num-1]+'.json', encoding='utf-8-sig', mode='r') as f:
			data = json.load(f)
		result = ['None']	
		w_cnt = 0
		for i in range(0, len(data)):
			if data[i]['word'] == wordname:
				result.pop()
				result.append(data[i]['polarity'])	
				w_cnt += 1 

		s_word = result[0]

		return s_word, w_cnt 

 # class CatSenti() :
	# def data_list(wordname):	
	# 	with open('data/food_info.json', encoding='utf-8-sig', mode='r') as f:
	# 		data = json.load(f)
	# 	result = ['None','None']	
	# 	w_cnt = 0
	# 	for i in range(0, len(data)):
	# 		if data[i]['word'] == wordname:
	# 			result.pop()
	# 			result.pop()
	# 			result.append(data[i]['word_root'])
	# 			result.append(data[i]['polarity'])	
	# 			w_cnt += 1 

	# 	r_word = result[0]
	# 	s_word = result[1]

	# 	print('word ' , r_word)
	# 	print('polority ',s_word)


	# 	return s_word, w_cnt 
