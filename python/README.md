<p align="center">
    <a href="https://smartproxy.com/"><img src="https://snipboard.io/3IyORg.jpg" alt="Smartproxy logo"></a>
  </a>
</p>

<p align="center">
    <a href="https://github.com/Smartproxy/Smartproxy"> :house: Main Repository :house: </a>
</p>

### Disclaimer

Selenium is a browser automation tool. This particular repository only covers Selenium setup for the Python programming language.

To continue further development with this tool, read the official Selenium [documentation](https://selenium-python.readthedocs.io/) for Python.

*Unfortunately, Selenium itself doesn't support `username:password` authentication for `HTTP/HTTPs` proxies; therefore, you'll need to have your IP whitelisted.*

You can do that by following the guidelines listed [here](https://help.smartproxy.com/docs/residential-authentication-methods#section-whitelisted-ip).

### Prerequisites

- [Python](https://www.python.org/downloads/)
- [Selenium](https://seleniumhq.github.io/selenium/docs/api/py/index.html#installing)

### Installation

Once you have all of the prerequisites ready, open the Terminal/Command Prompt window and create your project folder:

```
mkdir your_project
```
<img src="https://snipboard.io/jWxpiu.jpg">

When the project directory is set up, you can download the script *example.py*:
1. Navigate to the main directory of your project folder using `cd your_project`
2. Download the script using the following command: `curl https://raw.githubusercontent.com/Smartproxy/Selenium/master/python/example.py > example.py`
<img src="https://snipboard.io/4SdKnL.jpg">
3. Your project folder should now be populated with the *example.py* file.


### Configuration

The only configuration required for the script are the values below:

```
HOSTNAME = ''
PORT = ''
DRIVER = ''
```

You can get the `HOSTNAME` and `PORT` information from the [Smartproxy dashboard](https://dashboard.smartproxy.com/).

The configuration for the `DRIVER` value can be either 'CHROME' or 'FIREFOX'. This will determine if 'chromedriver' or 'geckodriver' will be installed and used during the process.

### Usage

The script consists of two functions:
- `smartproxy()` – handles the proxy authentication;
- `webdriver_example()` – installs the required drivers and gets a response from the target. In this case, the target is `http://ip.smartproxy.com/`.

```
browser.get('http://ip.smartproxy.com/')
```

Note that Chrome and Firefox have different attributes for proxy authentication; therefore, your requests should be similar to the following:

*Firefox*

```
browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()), proxy=smartproxy())
```

*Chrome*

```
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), desired_capabilities=smartproxy())
```

### Testing

Before proceeding with the testing, you'll need to install the `webdriver_manager` using the command below:
```
pip3 install webdriver_manager
```

To run the script, simply execute the `python3 example.py` command while in your project's directory.
<img src="https://snipboard.io/sPyz1D.jpg">

For machines running Windows, execute the `python example.py` command instead.

## Need help?
Email - sales@smartproxy.com
<br><a href="https://smartproxy.com">Live chat 24/7</a>
