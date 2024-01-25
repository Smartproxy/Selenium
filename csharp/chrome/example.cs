using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

class Program
{
    static void Main(string[] args)
    {
        ChromeOptions options = new ChromeOptions();

        var proxy = new Proxy
        {
            Kind = ProxyKind.Manual,
            IsAutoDetect = false,
            HttpProxy = "http://gate.smartproxy.com:7000"       //Proxy host:port configuration
        };
        options.Proxy = proxy;

        IWebDriver driver = new ChromeDriver(options);
        driver.Navigate().GoToUrl("http://ip.smartproxy.com/"); //Target website
        var getBody = driver.FindElement(By.TagName("body"));
        var getBodyText = getBody.Text;

        Console.WriteLine(getBodyText);

        driver.Quit();
    }
}
