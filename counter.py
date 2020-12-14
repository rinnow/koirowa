from selenium import webdriver
import time
import csv
import os
import shutil

votes1 = {}
votes = {}
voted = {}
array = []

#chromeを開きます 適宜firefoxなどに変更できます
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path='./chromedriver', options=options)

#driver = webdriver.Chrome('./chromedriver')
#chrome開くのはこれだけでもOK

#votes.csvが存在する倍はvoted.csvを作成
if (os.path.exists("./votes.csv"))==True:
    if (os.path.exists("./voted.csv"))==True:
        os.remove("./voted.csv")
    shutil.copyfile("./votes.csv", "./voted.csv")

#各キャラクターのページを開き投票数をカウント
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
    votes1[counter]=name

#投票数で降順にしてリストに入れる
votes1 = sorted(votes1.items(), reverse=True)

#もしvoted.csvがある場合今回の結果と比較
if (os.path.exists("./voted.csv")) == True:
    for i in votes1:
        votes[i[0]]=i[1]
    
    with open('./voted.csv', 'r') as f:
        reader = csv.reader(f)
        for i in reader:
            voted[i[0]]=i[1]
            
    for i in votes.items():
        for j in voted.items():
            if i[1] == j[1]:
                num = int(i[0])-int(j[0])
                array.append([int(i[0]),i[1],'+'+str(num)])
else:
    array = votes1

#chromeを閉じる
driver.close()

#結果を書き込み
with open('votes.csv', 'w') as f:
    w = csv.writer(f, lineterminator='\n')
    for i in array:
        w.writerow(i)

