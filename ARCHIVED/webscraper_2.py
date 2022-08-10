from HTTP import requests

url = 'https://www.tedbaker.com/row/Mens/c/category_mens' ##Selenium WebDriver is a web framework that permits you to execute cross-browser tests. This tool is used for automating web-based application testing to verify that it performs expectedly
browser = webdriver.Chrome() ## A ChromeDriver is a separate executable or a standalone server that Selenium WebDriver uses to launch Google Chrome
browser.get(url)

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)


browser.find_element_by_xpath().click() ## Basically finds the xpath element on website.
