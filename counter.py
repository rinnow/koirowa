from selenium import webdriver
import time
import csv

votes = {}
	
driver = webdriver.Chrome('./chromedriver')

for i in range(13):
    name=''
    if i == 4:
        continue
    driver.get('https://www.asa-pro.com/koirowa/character/chara'+str(i+1)+'.html')
    time.sleep(1)
    counter = driver.find_element_by_id('counter').text
    counter = int(counter)
    char = driver.find_element_by_class_name('chara-data-set')
    char = char.text
    char = char[3:]
    for j in char:
        if j == '（':
            break
        else:
            name += j
    votes[counter]=name
    
#print(name)
votes = sorted(votes.items(), reverse=True)
#print(votes)
with open('votes.csv', 'w') as f:
    w = csv.writer(f, lineterminator='\n')
    for i in votes:
        w.writerow(i)