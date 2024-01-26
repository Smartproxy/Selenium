require('chromedriver');

var webdriver = require('selenium-webdriver'), By = webdriver.By,
    until = webdriver.until,  chrome = require("selenium-webdriver/chrome");  //Configures the Chromedriver

let addr = 'gate.smartproxy.com:7000'                                         //Proxy host:port configuration
let opt = new chrome.Options().addArguments(`--proxy-server=http://${addr}`)

var driver = new webdriver.Builder()                                          //Initializes the configured Chromedriver
 .forBrowser('chrome')
 .setChromeOptions(opt)
 .build();

driver.get('http://ip.smartproxy.com/')                                       //Target website

var textPromise = driver.findElement(webdriver.By.css('body')).getText();     //Select desired Element from your target website
textPromise.then((text) => {
  console.log(text);
});
