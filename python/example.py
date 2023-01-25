from selenium import webdriver
from selenium_python import get_driver_settings, smartproxy
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def webdriver_example():
  driver = get_driver_settings()
  if driver['DRIVER'] == 'FIREFOX':
    browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()), proxy=smartproxy())
  elif driver['DRIVER'] == 'CHROME':
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), desired_capabilities=smartproxy())
  browser.get('http://ip.smartproxy.com/')
  print(browser.page_source)
  browser.close()
if __name__ == '__main__':
  webdriver_example()
