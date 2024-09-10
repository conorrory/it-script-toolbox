#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Insert the WebSites Username and Password
username = ''
password = ''

#Selenium Driver
chromedriver = 'C:\\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)

#Insert WebSite URL
browser.get((''))


#Username Field
usernameField = browser.find_element_by_id('loginusername')
usernameField.send_keys(username)

#Finds the Next Field
nextTextField = browser.find_element_by_id('loginpassword')
nextTextField.click()


#Login Field
passwordField = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "loginpassword")))
passwordField.send_keys(password)


#LogIn Button
logInButton = browser.find_element_by_id('submitter1')
logInButton.click()
