from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import numpy as np
import pandas as pd
from hanspell import spell_checker 

df = pd.read_csv("rmEmoji_Review.csv")

reviews = np.array(df['ORIGINAL'][8000:].tolist())

driver = webdriver.Chrome()
driver.get("https://speller.cs.pusan.ac.kr")


#reviews = ["분위기 좋고 강추해요 커피 존맛", "커피 맛있어요"]

busan_list = []

for review in reviews : 

	if pd.isna(review) : pass

	else : 

		elem = driver.find_element_by_name("text1")
		
		elem.send_keys(review)
		#field enter 
		elem.send_keys(Keys.RETURN)

		check = driver.find_element_by_id("btnCheck")
		check.click()

		entity_num = 0 

		while True: 
			try: 
				driver.find_element_by_xpath('//*[@id="tdReplaceWord_'+str(entity_num)+'"]/ul/li/a').click() 
				entity_num += 1
			except: 
				break 
		
		try :
			elem_chk = driver.find_element_by_xpath('//*[@id="tdReplaceWord_0"]/ul/li/a')

			spell_chk= driver.find_element_by_xpath('//*[@id="tdCorrection1stBox"]').text
			busan_list.append(spell_chk)

			renew = driver.find_element_by_id("btnRenew2").click()
		except :
			busan_list.append(review)
			renew = driver.find_element_by_id("btnRenew2").click()

driver.quit()

print("~END~")

# naver_list=[]

# for review in busan_list : 
# 	#print(review)
# 	chk = spell_checker.check(review)
# 	naver_list.append(chk.checked)

# t_list = [] 

# user = df['UESR']
# score = df['SCORE']
# review = df['ORIGINAL']

# for item in zip(busan_list) : 
# 		t_list.append(
# 		[ 
# 			item[0],
# 			item[1],
# 		]
# 	)

nDf = pd.DataFrame(busan_list, columns =['BUSAN']) 
nDf.to_csv('spellchk_4.csv',index = False,  encoding = 'utf-8-sig')

#naver_list=[]

# for review in reviews : 
# 	#print(review)
# 	chk = spell_checker.check(review)
# 	naver_list.append(chk.checked)

# driver = webdriver.Chrome()
# driver.get("https://speller.cs.pusan.ac.kr")


# #reviews = ["분위기 좋고 강추해요 커피 존맛", "커피 맛있어요"]

# busan_list = []

# for review in naver_list : 

# 	if pd.isna(review) : pass

# 	else : 

# 		elem = driver.find_element_by_name("text1")
		
# 		elem.send_keys(review)
# 		#field enter 
# 		elem.send_keys(Keys.RETURN)

# 		check = driver.find_element_by_id("btnCheck")
# 		check.click()

# 		entity_num = 0 

# 		while True: 
# 			try: 
# 				driver.find_element_by_xpath('//*[@id="tdReplaceWord_'+str(entity_num)+'"]/ul/li/a').click() 
# 				entity_num += 1
# 			except: 
# 				break 
		
# 		try :
# 			elem_chk = driver.find_element_by_xpath('//*[@id="tdReplaceWord_0"]/ul/li/a')

# 			spell_chk= driver.find_element_by_xpath('//*[@id="tdCorrection1stBox"]').text
# 			busan_list.append(spell_chk)

# 			renew = driver.find_element_by_id("btnRenew2").click()
# 		except :
# 			busan_list.append(review)
# 			renew = driver.find_element_by_id("btnRenew2").click()

# driver.quit()

# t_list = [] 

# for item in zip(busan_list,naver_list) : 
# 		t_list.append(
# 		[ 
# 			item[0],
# 			item[1],
# 		]
# 	)

# nDf = pd.DataFrame(t_list, columns =['NAVER_BUSAN','NAVER']) 
# nDf.to_csv('spellchk_NAVER.csv',index = False, header = False, encoding = 'utf-8-sig')

# stateElemnentReferenceException error 
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import StaleElementReferenceException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions

# my_element_id = 'text1'
# ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
# your_element = WebDriverWait(dv,2,ignored_exceptions=ignored_exceptions).until(expected_conditions.presence_of_element_located((By.ID, my_element_id)))