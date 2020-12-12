from selenium import webdriver

	
driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.asa-pro.com/koirowa/character/chara6.html')
counter = driver.find_element_by_id('counter')
print(counter.text)