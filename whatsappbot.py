# spam spam spam
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://web.whatsapp.com/')

print("login")

name = input("Enter name : ")
count = int(input("Count : "))
message = input("message : ")

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msgBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

for i in range(count):
    msgBox.send_keys(message)
    sendButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]')
    sendButton.click()
