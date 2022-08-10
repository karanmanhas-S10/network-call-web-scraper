#Installing AutoHotKey (https://www.autohotkey.com/)  Script to trigger ChromeInspector



from selenium import webdriver

url = 'https://master.d6nia0rm2gj9k.amplifyapp.com/' ##Selenium WebDriver is a web framework that permits you to execute cross-browser tests. This tool is used for automating web-based application testing to verify that it performs expectedly
browser = webdriver.Chrome() ## A ChromeDriver is a separate executable or a standalone server that Selenium WebDriver uses to launch Google Chrome
browser.get(url)


#Triggering Chrome Inspector
import os
os.system("path_to_script.ahk/script.ahk")

##Fixing Webdriver issue
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)


''' 
String  openDevTools = Keys.chord(Keys.ALT, Keys.CONTROL, "i");
driver.findElement(By.ByTagName("body")).sendKeys(openDevTools);
'''

###LocalStorageSize = browser.getLocalStorageSize()


browser.close(url)

''' 
# Get Named Cookie Information 
cookie = {'name' : 'foo', 'value' : 'bar'}
browser.get_cookies() # Outputs all cookies for available URL
print (cookie("_ga"))
'''
### Code to open Chrome Developer tools
''' 
import configs  {
  chrome : {
    maxInstances: "5",
    browserName: "chrome",
    chromeOptions: {
      args: ['--window-size=1280,800', '--auto-open-devtools-for-tabs'],
      binary: '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome'
    }
  },
  firefox : {
    maxInstances: "5",
    browserName: "firefox"
  },
  headless : {
    maxInstances: "5",
    browserName: "chrome",
    chromeOptions: {
      args: ['--headless', '--disable-gpu', '--window-size=1280,800'],
      binary: '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome'
    }
  },
  ''' 