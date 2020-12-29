from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
from html_table_parser import parser_functions as parser

a=input("검색할 키워드를 입력하세요 : ")
driver = webdriver.Chrome()
driver.get('https://whereispost.com/keyword/#')
elem = driver.find_element_by_name("keyword")
elem.send_keys(a)
elem.send_keys(Keys.RETURN)

keyword=driver.find_element_by_xpath('//*[@id="result"]/tbody')

print(keyword.text)

"""
images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 0
for image in images:
    try:
        image.click()
        time.sleep(2)
        imgUrl = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img").get_attribute("src")
        urllib.request.urlretrieve(imgUrl, "imgfile/" + a + str(count) + ".jpg")
        count += 1
        if count == b:
            break
    except:
        pass
driver.close()
"""