using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using OpenQA.Selenium;
using OpenQA.Selenium.Firefox;

class Program
{
    static void Main(string[] args)
    {
        FirefoxOptions options = new FirefoxOptions();           //Configures the Geckodriver

        var proxy = new Proxy
        {
            Kind = ProxyKind.Manual,
            IsAutoDetect = false,
            HttpProxy = "gate.smartproxy.com:7000"               //Proxy host:port configuration
        };
        options.Proxy = proxy;

        IWebDriver driver = new FirefoxDriver(options);          //Initializes the configured Geckodriver
        driver.Navigate().GoToUrl("http://ip.smartproxy.com/");  //Target website
        var getBody = driver.FindElement(By.TagName("body"));    //Select desired Element from your target website
        var getBodyText = getBody.Text;

        Console.WriteLine(getBodyText);

        driver.Quit();
    }
}
