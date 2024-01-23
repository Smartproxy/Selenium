<p align="center">
    <a href="https://smartproxy.com/"><img src="https://snipboard.io/3IyORg.jpg" alt="Smartproxy logo" width="200" height="50"></a>
  </a>
</p>

<p align="center">
    <a href="https://github.com/Smartproxy/Smartproxy"> :house: Main Repository :house: </a>
</p>

### Disclaimer

Selenium is a browser automation tool. This particular repository only covers Selenium setup for Python based programming language.

To continue further development with this tool, make sure to read their [documentation](https://selenium-python.readthedocs.io/) for Python.

*Unfortunately, Selenium itself does not support `username:password` authentication for `HTTP/HTTPs` proxies, thus you will need to have your IP whitelisted.*

You can do that by following guidlines listed [here](https://help.smartproxy.com/docs/residential-authentication-methods#section-whitelisted-ip).

### Prerequisites

- [Python](https://www.python.org/downloads/)
- [Selenium](https://seleniumhq.github.io/selenium/docs/api/py/index.html#installing)

### Installation

Once you have all the prerequisites ready, open Terminal/Command Prompt window and create your project folder:

```
mkdir your_project
```
<img src="https://snipboard.io/jWxpiu.jpg">

When project directory is setup, you can download our script example.py:
1. Navigate to the main directory of your project folder using `cd your_project`
2. Download our script using the following command: `curl https://raw.githubusercontent.com/Smartproxy/Selenium/master/python/example.py > example.py`
<img src="https://snipboard.io/4SdKnL.jpg">
3. You should now see your project folder populated with *example.py* file.


### Configuration

Only configuration required for our script are the values bellow:

```
HOSTNAME = ''
PORT = ''
DRIVER = ''
```

You can get information for `HOSTNAME` and `PORT` on our [users dashboard pannel](https://dashboard.smartproxy.com/).

The configuration for `DRIVER` value can be either 'CHROME' or 'FIREFOX'. This will determine if 'chromedriver' or 'geckodriver' will be installed and used during the process.

<img src="https://snipboard.io/IO2tPD.jpg">

### Usage

The script consists of two functions `smartproxy()` - which handles the proxy authentication and `webdriver_example()` - which installs required drivers and gets a response from your target, in this case the target is `http://ip.smartproxy.com/`

```
browser.get('http://ip.smartproxy.com/')
```

Note that Chrome and Firefox have different attributes for proxy authentication, thus your requests should look along these lines:

*Firefox*

```
browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()), proxy=smartproxy())
```

*Chrome*

```
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), desired_capabilities=smartproxy())
```

### Testing

Before proceeding with the testing, you will need to install the `webdriver_manager` using the command bellow:
```
pip3 install webdriver_manager
```

In order to run our script, simply execute `python3 example.py` command while in your project directory.
<img src="https://snipboard.io/sPyz1D.jpg">

Note: for machines running Windows, execute `python example.py` command instead.

## Need help?
Email - sales@smartproxy.com
<br><a href="https://smartproxy.com">Live chat 24/7</a>
