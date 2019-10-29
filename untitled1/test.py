from bs4 import BeautifulSoup
import requests
from selenium import webdriver
browser = webdriver.Chrome('/home/ganesh/Downloads/chromedriver')
browser.get('https://www.flipkart.com')
try:
    abc = browser.find_element_by_xpath("//div[@class ='_3Njdz7']//button[@class = '_2AkmmA _29YdH8']")
    abc.click()
except:
    print("hi")
print(abc)
mob = browser.find_element_by_id('container')
inputs = mob.find_element_by_class_name('LM6RPg')
inputs.send_keys('Mobiles')
clicked = mob.find_element_by_class_name('vh79eN').click()
print("---------------------------------------")
#print(mob.text)
acb = browser.find_element_by_xpath("//div[@id = 'container']")
full = acb.find_element_by_tag_name('div')
#acb.find_element_by_xpath("//div[@class = 't-0M7P _2doH3V']")
print(full.text)
