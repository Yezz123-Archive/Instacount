﻿from selenium import webdriver
from random import randint
import time
import Generator as account

browser = webdriver.Chrome("chrome web driver path here")
browser.get("http://www.instagram.com")
# time.sleep count can be changed depending on the Internet speed.
time.sleep(8)
name = account.username()

# Fill the email value
email_field = browser.find_element_by_name('emailOrPhone')
email_field.send_keys(account.generatingEmail())
print(account.generatingEmail())

# Fill the fullname value
fullname_field = browser.find_element_by_name('fullName')
fullname_field.send_keys(account.generatingName())
print(account.generatingName())
# Fill username value
username_field = browser.find_element_by_name('username')
username_field.send_keys(name)
print(name)
# Fill password value
password_field = browser.find_element_by_name('password')
# You can determine another password here.
password_field.send_keys('aa12345bb12345cc'+name)

# browser find react-root
submit = browser.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[6]/span/button')
submit.click()
time.sleep(8)

print('Registering....')
