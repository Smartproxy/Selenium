from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

HOSTNAME = 'us.smartproxy.com' #Proxy host:port configuration
PORT = '10000'
DRIVER = 'CHROME' #Select 'CHROME' or 'FIREFOX'

def smartproxy(): #Selects appropriate driver and sets up proxy
    if DRIVER == 'FIREFOX':
        options = FirefoxOptions()
    elif DRIVER == 'CHROME':
        options = ChromeOptions()
    else:
        raise ValueError("Invalid driver specified")

    proxy_str = '{hostname}:{port}'.format(hostname=HOSTNAME, port=PORT)
    options.add_argument('--proxy-server={}'.format(proxy_str))

    return options

def webdriver_example(): #Installs the latest selected webdriver and uses proxy to reach target
    if DRIVER == 'FIREFOX':
        browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()), 
                                    options=smartproxy())
    elif DRIVER == 'CHROME':
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), 
                                   options=smartproxy())
    browser.get('http://ip.smartproxy.com/ip') #Target URL
    print(browser.page_source) #Prints out desired element of target URL
    browser.quit()

if __name__ == '__main__':
    webdriver_example()
