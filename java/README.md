<p align="center">
    <a href="https://smartproxy.com/"><img src="https://snipboard.io/3IyORg.jpg"></a>
  </a>
</p>

<p align="center">
    <a href="https://github.com/Smartproxy/Smartproxy"> :house: Main Repository :house: </a>
</p>

### Disclaimer

Selenium is a browser automation tool. This particular repository only covers Selenium setup for Java based programming language.

To continue further development with this tool, make sure to read their [documentation](https://seleniumhq.github.io/selenium/docs/api/java/index.html) for Java.

*Unfortunately, Selenium itself does not support `username:password` authentication for `HTTP/HTTPs` proxies, thus you will need to have your IP whitelisted.*

You can do that by following guidlines listed [here](https://help.smartproxy.com/docs/proxy-authentication).

### Prerequisites

- [Java](https://www.java.com/en/)
- [Java SE Runtime Environment 8](https://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html)
- [Selenium Server 3.9.1](https://selenium-release.storage.googleapis.com/3.9/selenium-server-3.9.1.zip)
- [Selenium Server Standalone JAR](https://selenium-release.storage.googleapis.com/3.9/selenium-server-standalone-3.9.1.jar)

Optional:
- [Chrome WebDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- [Firefox WebDriver](https://github.com/mozilla/geckodriver/releases)

Note that you need to have at least one of the above drivers to continue your progress.

### Installation

This particular code was built with [Eclipse](https://www.eclipse.org/) which will be used to build and launch the application.

If you feel like using something else or executing the script with `javac` command, you may need to install [JAVA JRE](https://www.oracle.com/technetwork/java/javase/downloads/server-jre8-downloads-2133154.html).

Once you have all the prerequisites ready, create your project folder:

```
mkdir your_project
```
<img src="https://i.imgur.com/6US2PJs.png">

When project directory is setup, you can now download our example script for Selenium.

Make sure that you download the script accordingly to which WebDriver you want to use:

1. Open Terminal/Command Prompt window.
2. Navigate to the main directory of your project folder using `cd your_project`
3. Download one of the examples below.
4. You should now see your project folder populated with *example.java* file.

*Firefox*

```
curl https://raw.githubusercontent.com/Smartproxy/Selenium/master/java/firefox/example.java > example.java
```

*Chrome*

```
curl https://raw.githubusercontent.com/Smartproxy/Selenium/master/java/chrome/example.java > example.java
```

### Configuration

To configure the proxy, simply change the following strings in the code:

```
String ProxyServer = "gate.smartproxy.com"; #Location you want to target
int ProxyPort = 7000; #Port for session
```

<img src="https://i.imgur.com/RfCa9xV.png" alt="smartproxy selenium java http proxy setup">

### Testing

If everything is done correctly, after running the code, selected WebDriver will apear with a new IP from the proxy service:

<img src="https://i.imgur.com/EUbzHh4.png">

You will also get a printed output of the IP in the Console:

<img src="https://i.imgur.com/tBbOAlA.png">

## Need help?
Email - sales@smartproxy.com
<br><a href="https://smartproxy.com">Live chat 24/7</a>
