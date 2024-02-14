<p align="center">
    <a href="https://smartproxy.com/"><img src="https://snipboard.io/3IyORg.jpg"></a>
  </a>
</p>

<p align="center">
    <a href="https://github.com/Smartproxy/Smartproxy"> :house: Main Repository :house: </a>
</p>

### Disclaimer

Selenium is a browser automation tool. This repository only covers Selenium setup for the Node.js (Javascript) programming language.

To continue further development with this tool, make sure to read the official Selenium [documentation](https://github.com/SeleniumHQ/selenium/tree/master/javascript/node/selenium-webdriver).

*Unfortunately, Selenium itself doesn't support `username:password` authentication for `HTTP/HTTPs` proxies; therefore you'll need to have your IP whitelisted.*

You can do that by following the guidelines listed [here](https://help.smartproxy.com/docs/residential-authentication-methods).

### Prerequisites

- [Node](https://nodejs.org/en/download/)
- [Selenium](https://github.com/SeleniumHQ/selenium/tree/master/javascript/node/selenium-webdriver#installation)

Optional:
- [Chrome WebDriver](https://www.npmjs.com/package/chromedriver#building-and-installing)
- [Firefox WebDriver](https://www.npmjs.com/package/geckodriver#install)

You'll need to install at least one of the above WebDrivers in the [Installation](#installation) part.

### Installation

1. Once you have all the required prerequisites ready, create your project folder:

```
mkdir node_selenium
cd node_selenium
npm init
npm install selenium-webdriver
```
<img src="https://i.imgur.com/53kgOXn.png">

2. When the project directory is set up, you'll need to install one of the WebDrivers from the [Prerequisites](#prerequisites) section.

*Firefox*

<img src="https://i.imgur.com/I9czv1a.png">

*Chrome*

<img src="https://i.imgur.com/ALgnAQf.png">

3. Download the example script according to the WebDriver you are using with one of these commands: 

*Firefox*

```curl https://raw.githubusercontent.com/Smartproxy/Selenium/master/nodejs/firefox/example.js > example.js```

*Chrome*

```curl https://raw.githubusercontent.com/Smartproxy/Selenium/master/nodejs/chrome/example.js > example.js```

4. Your project folder should now be populated with the *example.js* file.

### Configuration

To configure the example script with a different endpoint, simply edit the `let addr =` line in within punctuation marks('') as in the example:

<img src="https://i.imgur.com/rBL5rWw.png" alt="smartproxy selenium node.js http proxy configuration example">

### Usage

You can test the script by running the `node example.js` command while in your project folder.

A browser window will appear with the targeted website, and a proxy IP should be visible in the console output:

<img src="https://i.imgur.com/7Na6wEN.png">

## Need help?
Email - sales@smartproxy.com
<br><a href="https://direct.lc.chat/12092754/">Live chat 24/7</a>
