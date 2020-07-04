from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import string
import re
import time
browser = webdriver.Chrome('/home/ganesh/Downloads/chromedriver')
browser.get('http://keapu-webugpp01-in.cloudapp.net:84/pgetresults2020-r1/main/results.php')
delay = 3
alpha = list(string.ascii_uppercase)
alpha = alpha[0:6]
file = open('rank1.txt','a')
#for a in alpha:
for i in range(10):
    #for j in range(10):
    for alpa in alpha:
        #for k in range(10):
        for alphabet in alpha :
            #val = 'M1' +  str(i) + str(j) + str(k)
            #val =  'M1' + a + alpa + alphabet
            #val = 'M1' + str(i) + str(j) + alpa
            #val = 'M1' + str(i) + alpa + str(j)
            # val = 'M1' + alpa + str(i)  + str(j)
            val = 'M2'  + alpa + str(i) +  alphabet
            store = browser.find_element_by_xpath('/html/body/table[2]/tbody/tr[9]/td/form/table/tbody/tr[2]/td[2]/input')
            store.send_keys(val)
            clickable = browser.find_element_by_xpath('/html/body/table[2]/tbody/tr[9]/td/form/table/tbody/tr[3]/td[2]/input')
            clickable.click()
        # Invalid =
        # not_alloted =
        # print(Invalid)
        # print(not_alloted)
        # the_num = re.search("Invalid PGET number", Invalid)
        # not_alloted = re.search("You have not been allotted any Medical seat",not_alloted)
            if(re.search("Invalid PGET number",browser.find_element_by_tag_name('span').text)):
                abc = browser.find_element_by_link_text('Back')
            # time.sleep(2)
                abc.click()
                continue
            elif(re.search("You have not been allotted any Medical seat",browser.find_element_by_xpath('/html/body/table[2]/tbody/tr[5]/td/table/tbody/tr/td/font/b/span').text)):
                abc = browser.find_element_by_link_text('Back')
            # time.sleep(2)
                abc.click()
                continue
            else:
                browser.implicitly_wait(10)
                full = browser.find_element_by_xpath('/html/body/table[2]/tbody/tr[5]/td/table[1]/tbody/tr[2]/td/table/tbody/tr/td[2]/table').text
            # name = browser.find_element_by_xpath('/html/body/table[2]/tbody/tr[5]/td/table[1]/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td[2]/font/span/span').text
            # Rank = browser.find_element_by_xpath('/html/body/table[2]/tbody/tr[5]/td/table[1]/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[7]/td[2]/font/span').text
            # College = browser.find_element_by_xpath('/html/body/table[2]/tbody/tr[5]/td/table[1]/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[11]/td[2]/font/b/span').text
            # Subject = browser.find_element_by_xpath('/html/body/table[2]/tbody/tr[5]/td/table[1]/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[13]/td[2]/font/b/span').text
            # print(name)
            # print(Rank)
            # print(College)
                file.write(full)
                file.write("-----------------------------------------------------------")
            #            print(full)
            #           print("------------------------------------------------------------------------------------------------------------------------------")
                abc = browser.find_element_by_link_text('Back')
                #time.sleep(2)
                abc.click()
file.close()
browser.close()

#/html/body/table[2]/tbody/tr[5]/td/table[1]/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td[2]/font/span/span