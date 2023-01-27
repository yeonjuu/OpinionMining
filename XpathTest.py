import sys
from selenium import webdriver 
import time 
import pandas as pd 
from selenium.common.exceptions import NoSuchElementException
import numpy as np

#restaurant/(카페이름) /review~ 이런식의 url  
#url ='http://pcmap.place.naver.com/restaurant/1921874344/review/visitor?entry=pll&from=map&ts=20210512'
#url='https://pcmap.place.naver.com/restaurant/1425989301/review/visitor?entry=plt&from=map&fromPanelNum=1&ts=1623938155375'
#url ='https://pcmap.place.naver.com/restaurant/34572827/review/visitor?entry=pll&from=map&fromPanelNum=2&ts=16239449148#27'
#url='https://pcmap.place.naver.com/restaurant/1030871168/review/visitor?from=map&fromPanelNum=1&ts=1623947674396'
#url = 'https://pcmap.place.naver.com/restaurant/1200009607/review/visitor?entry=plt&from=map&fromPanelNum=1&ts=1624020716727'
#url='https://pcmap.place.naver.com/restaurant/1395030685/review/visitor?entry=plt&from=map&fromPanelNum=1&ts=1624022773923'
#url = 'https://pcmap.place.naver.com/restaurant/1725895520/review/visitor?entry=pll&from=map&fromPanelNum=2&ts=1624031212661'
#url = 'https://pcmap.place.naver.com/restaurant/1432336976/review/visitor?entry=plt&from=map&fromPanelNum=1&ts=20210512'

url = 'https://pcmap.place.naver.com/restaurant/1425989301/review/visitor?entry=plt&from=map&fromPanelNum=1&ts=1627151749290'
#website loading
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=options)

driver.implicitly_wait(15) 
driver.get(url)

while True:
    try:
        morebtn = driver.find_element_by_css_selector('a._3iTUo')
        morebtn.click()
        time.sleep(1)
    except:
        break

#total = driver.find_elements_by_css_selector('div.hbo4A') 
rvs = driver.find_elements_by_css_selector('span.WoYOw')
reviews =[]
for review in rvs: 
	reviews.append(review.text)
	
users=[]
scores=[]

#total = int(len(reviews))+1
#print("total review : "+total)

for i in range(1,365) : 
	try:
		#사진이 없는 리뷰일 경우의 리뷰 경로
		check = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[5]/div[4]/div[4]/div[1]/ul/li['+str(i)+']/div/div[3]/a/span')
				
		user = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[5]/div[4]/div[4]/div[1]/ul/li['+str(i)+']/div/div[1]/a/div/div[1]')
		score = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[5]/div[4]/div[4]/div[1]/ul/li['+str(i)+']/div/div[2]/div[1]/span[2]')
		#review=driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[5]/div[4]/div[4]/div[1]/ul/li['+str(i)+']/div/div[3]/a/span')
		users.append(user.text)
		scores.append(score.text)
		#reviews.append(review.text)

	except NoSuchElementException :
		try:
			#사진이 포함된 리뷰일 경우의 리뷰 경로
			check2 = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[5]/div[4]/div[4]/div[1]/ul/li['+str(i)+']/div/div[4]')

			user2 =driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[5]/div[4]/div[4]/div[1]/ul/li['+str(i)+']/div/div[1]/a/div/div[1]')
			score2 =driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[5]/div[4]/div[4]/div[1]/ul/li['+str(i)+']/div/div[3]/div[1]/span[2]')
			#review2=driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[5]/div[4]/div[4]/div[1]/ul/li['+str(i)+']/div/div[4]/a/span')
			users.append(user2.text)
			scores.append(score2.text)
			#reviews.append(review2.text)

		except NoSuchElementException :
			try : 
				check3 = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[5]/div[4]/div[4]/div[1]/ul/li['+str(i)+']/div/div[5]')
				
				user3 =driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[5]/div[4]/div[4]/div[1]/ul/li['+str(i)+']/div/div[1]/a/div/div[1]')
				score3 =driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[5]/div[4]/div[4]/div[1]/ul/li['+str(i)+']/div/div[3]/div[1]/span[2]')

				users.append(user3.text)
				scores.append(score3.text)
			except :
				print(i)

#변수 합치기 , csv변환	
rv_list=[]		
for item in zip(users, scores, reviews): 
	rv_list.append( 
		[ 
			item[0], 
			item[1], 
			item[2], 
		] 
	) 

rv_infos = pd.DataFrame(rv_list, columns=['USER', 'SCORE', 'REVIEW']) 
rv_infos.to_csv('17.Granpafactory.csv', encoding='utf-8-sig') 
print("END")

driver.quit()

