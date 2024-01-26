require('geckodriver');

var webdriver = require('selenium-webdriver'), By = webdriver.By,
    until = webdriver.until,  firefox = require("selenium-webdriver/firefox"), proxy = require('selenium-webdriver/proxy');

let addr = 'gate.smartproxy.com:7000'    //Proxy host:port configuration

var driver = new webdriver.Builder()
 .forBrowser('firefox')
 .setProxy(proxy.manual({http: addr}))
 .build();

driver.get('http://ip.smartproxy.com/')  //Target website

var textPromise = driver.findElement(webdriver.By.css('body')).getText();
textPromise.then((text) => {
  console.log(text);
});
