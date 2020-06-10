from selenium import webdriver
from random import randint
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import account

#browser instance
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("http://www.instagram.com")
time.sleep(8) # time to change depending to internet speed
name = account.username()

#fill the email 
email = browser.find_element_by_name("emailOrPhone")
email.send_keys(account.genMail())
print(account.genMail())

#fill the fullname value
fullname =browser.find_element_by_name("fullName")
fullname.send_keys(account.genName())
print(account.genName())

# fill the usernmae
user = browser.find_element_by_name("username")
browser.send_keys(name)
print(name)

# fill password
pwd = browser.find_element_by_name("password")
browser.send_keys('aa12345bb12345cd'+name)

submit = browser.find_element_by_name('//*[@id="//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[6]/span/button')
submit.click()

time.sleep(8)

print("Registering....")