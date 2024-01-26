require('geckodriver');

var webdriver = require('selenium-webdriver'), By = webdriver.By,
    until = webdriver.until,  firefox = require("selenium-webdriver/firefox"), proxy = require('selenium-webdriver/proxy'); //Configures the Geckodriver

let addr = 'gate.smartproxy.com:7000'                                                                                       //Proxy host:port configuration

var driver = new webdriver.Builder()                                                                                        //Initializes the configured Geckodriver
 .forBrowser('firefox')
 .setProxy(proxy.manual({http: addr}))
 .build();

driver.get('http://ip.smartproxy.com/')                                                                                     //Target website

var textPromise = driver.findElement(webdriver.By.css('body')).getText();                                                   //Select desired Element from your target website
textPromise.then((text) => {
  console.log(text);
});
