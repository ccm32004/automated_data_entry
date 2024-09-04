import pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from function import automate, removeSpace, getDate


options = webdriver.ChromeOptions()

username = "username"
password = "password"
url = 'url of form'

options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)

driver.get(url)

driver.find_element(By.NAME, 'log').send_keys(username)
driver.find_element(By.NAME, 'pwd').send_keys(password)
driver.find_element(By.NAME,'wp-submit').click()

#post page
label = removeSpace(input("please input the label here thank you "))
print(label)
pdf = automate(label)
print(pdf)
date = getDate(label)
print(date)

driver.find_element(By.NAME, 'post_title').send_keys(label)
driver.find_element(By.ID, "acf-field_64375475b9971").send_keys(pdf)

#datebox
driver.find_element(By.ID, "acf-field_643754a3b9972").send_keys(date)

#archive button checkbox
driver.find_element(By.XPATH, '//*[@id="in-category-68"]' ).click()

#commit hyphen ver to clipboard
pdf = pdf.replace('.pdf', '')
pyperclip.copy(pdf)
test = pyperclip.paste()
print(test)

#publish
driver.find_element(By.NAME, 'publish' ).click()

#driver.find_element(By.XPATH,'//*[@id="menu-posts-family_archives"]/ul/li[2]/a').click()
time.sleep(10000)




