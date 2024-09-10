# it-script-toolbox
A collection of scripts I have written and used over the years in my time as an IT engineer. Nothing fancy. 

For the Auto Login Scripts: Note: Pythin required to be installed on the device for scripts using Selenium. 

Installing Python and Selenium on Windows

1. Install Python 3.6 - https://www.python.org/downloads/
	Make sure to install for all users
	Make sure to install into Program Files

2. Install Selenium - 
Run CMD as Administrator
Go to C:\Program Files\Python36\Scripts\
Type pip.exe install selenium
3. Download Selenium Drivers for Browser
Chrome:  https://sites.google.com/a/chromium.org/chromedriver/downloads
Edge:  https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
Firefox:  https://github.com/mozilla/geckodriver/releases
Safari:   https://webkit.org/blog/6900/webdriver-support-in-safari-10/
4. UnZip and Save the Driver to C:\\ folder
5. Open IDLE.
6. Open your Script – Select Run - Module (F5) 


To find the HTML ID in Chrome:
	Menu – More Tools – Developer Tools


Code that needs to be changed in Bold

#Insert the WebSites Username and Password
username = ''
password = ''


#Insert WebSite URL
browser.get((''))


#Username Field
usernameField = browser.find_element_by_id('loginusername')


#Finds the Next Field
nextTextField = browser.find_element_by_id('loginpassword')


#Login Field
passwordField = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "loginpassword")))


#LogIn Button
logInButton = browser.find_element_by_id('submitter1')
