from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.proxy import Proxy, ProxyType

HOSTNAME = ''
PORT = ''
DRIVER = ''

def smartproxy():
  prox = Proxy()
  prox.proxy_type = ProxyType.MANUAL
  prox.http_proxy = '{hostname}:{port}'.format(hostname = HOSTNAME, port = PORT)
  prox.ssl_proxy = '{hostname}:{port}'.format(hostname = HOSTNAME, port = PORT)
  if DRIVER == 'FIREFOX':
    capabilities = webdriver.DesiredCapabilities.FIREFOX
  elif DRIVER == 'CHROME':
    capabilities = webdriver.DesiredCapabilities.CHROME
  prox.add_to_capabilities(capabilities)
  return capabilities

def webdriver_example():
  if DRIVER == 'FIREFOX':
    browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()), proxy=smartproxy())
  elif DRIVER == 'CHROME':
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), desired_capabilities=smartproxy())
  browser.get('http://ip.smartproxy.com/')
  print(browser.page_source)
  browser.quit()

if __name__ == '__main__':
  webdriver_example()
