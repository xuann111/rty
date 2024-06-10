from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get('http://localhost:8000')

assert 'Django' in browser.page_source

time.sleep(5)
input("Press Enter to close the browser...")
browser.quit()