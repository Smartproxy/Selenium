<p align="center">
    <a href="https://smartproxy.com/"><img src="https://snipboard.io/3IyORg.jpg"></a>
  </a>
</p>

<p align="center">
    <a href="https://github.com/Smartproxy/Smartproxy"> :house: Main Repository :house: </a>
</p>

### Disclaimer

Selenium is a browser automation tool. This particular repository only covers Selenium setup using the Java programming language.

To continue further development with this tool, read Selenium's official [documentation](https://seleniumhq.github.io/selenium/docs/api/java/index.html) for Java.

*Unfortunately, Selenium itself doesn't support `username:password` authentication for `HTTP/HTTPs` proxies; therefore, you'll need to have your IP whitelisted.*

You can do that by following the guidelines listed [here](https://help.smartproxy.com/docs/residential-authentication-methods).

### Prerequisites

- [Java](https://www.java.com/en/)
- [Java SE Runtime Environment 8](https://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html)
- [Selenium Server 3.9.1](https://selenium-release.storage.googleapis.com/3.9/selenium-server-3.9.1.zip)
- [Selenium Server Standalone JAR](https://selenium-release.storage.googleapis.com/3.9/selenium-server-standalone-3.9.1.jar)

Optional:
- [Chrome WebDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- [Firefox WebDriver](https://github.com/mozilla/geckodriver/releases)

You'll need at least one of the above drivers to continue with the next steps.

### Installation

This code was built with [Eclipse](https://www.eclipse.org/), which will be used to build and launch the application.

If you feel like using something else or executing the script with the `javac` command, you may need to install [JAVA JRE](https://www.oracle.com/technetwork/java/javase/downloads/server-jre8-downloads-2133154.html).

Once you have all of the prerequisites ready, create your project folder:

```
mkdir your_project
```
<img src="https://i.imgur.com/6US2PJs.png">

When the project directory is set up, you can now download our example script for Selenium.

Make sure that you download the script according to which WebDriver you want to use:

1. Open the Terminal/Command Prompt window.
2. Navigate to the main directory of your project folder using `cd your_project`
3. Download one of the examples below.
4. You should now see your project folder populated with the *example.java* file.

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
String ProxyServer = "gate.smartproxy.com"; # Location you want to target
int ProxyPort = 7000; # Port for session
```

<img src="https://i.imgur.com/RfCa9xV.png" alt="smartproxy selenium java http proxy setup">

### Testing

If everything is done correctly, the selected WebDriver will appear with a new IP from the proxy service after running the code:

<img src="https://i.imgur.com/EUbzHh4.png">

You'll also get a printed output of the IP in the Console:

<img src="https://i.imgur.com/tBbOAlA.png">

## Need help?
Email - sales@smartproxy.com
<br><a href="https://direct.lc.chat/12092754/">Live chat 24/7</a>
