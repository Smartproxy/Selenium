package chromeScripts;

import java.io.File;

import org.openqa.selenium.By;
import org.openqa.selenium.Proxy;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeDriverService;
import org.openqa.selenium.chrome.ChromeOptions;

public class Example {

	public static void main(String[] args) {
		
		String ProxyServer = "gate.smartproxy.com";                                       //Proxy host:port configuration
		int ProxyPort = 7000;
		
		String sHttpProxy = ProxyServer + ":" + ProxyPort;
		
		Proxy proxy = new Proxy();
		
		proxy.setHttpProxy(sHttpProxy);
		
		ChromeDriverService service = new ChromeDriverService.Builder()                   //Initializes Chromedriver configuration
		                            .usingDriverExecutable(new File("PATH TO WEBDRIVER")) //Change the path to your Chromedriver
		                            .usingAnyFreePort()
		                            .build();
		ChromeOptions options = new ChromeOptions();
		
		options.setCapability("proxy", proxy);
		
		options.merge(options);                                                           //Initializes the configured Chromedriver
		
		WebDriver driver=new ChromeDriver(service, options);
		driver.get("http://ip.smartproxy.com/");                                          //Target website
	    WebElement body = driver.findElement(By.tagName("body"));                             //Select desired Element from your target website
	    String bodyText = body.getText();
		System.out.println(bodyText);
	}

}
