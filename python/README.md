<p align="center">
    <a href="https://smartproxy.com/"><img src="https://smartproxy.com/wp-content/themes/smartproxy/images/smartproxy-logo.svg" alt="Smartproxy logo" width="200" height="50"></a>
  </a>
</p>

<p align="center">
    <a href="https://github.com/Smartproxy/Smartproxy"> :house: Main Repository :house: </a>
</p>

### Disclaimer

Selenium is a browser automation tool. This particular repository only covers Selenium setup for Python based programming language.

To continue further development with this tool, make sure to read their [documentation](https://selenium-python.readthedocs.io/) for Python.

*Unfortunately, Selenium itself does not support `username:password` authentication for `HTTP/HTTPs` proxies, thus you will need to have your IP whitelisted.*

You can do that by following guidlines listed [here](https://help.smartproxy.com/docs/proxy-authentication).

### Prerequisites

- [Python](https://www.python.org/downloads/)
- [Selenium](https://seleniumhq.github.io/selenium/docs/api/py/index.html#installing)

Optional:
- [Chrome WebDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- [Firefox WebDriver](https://github.com/mozilla/geckodriver/releases)

Note that you need to have at least one of the above drivers to continue your progress.

### Installation

Once you have all the prerequisites ready, create your project folder:

```
mkdir your_project
```
<img src="https://i.imgur.com/6US2PJs.png">

When project directory is setup, you download our script for proxy authentication:

1. Open Terminal/Command Prompt window.
2. Navigate to the main directory of your project folder using `cd your_project`
3. Download our proxy middleware using the following command: `curl https://raw.githubusercontent.com/Smartproxy/Selenium/master/python/selenium_python.py > selenium_python.py`
<img src="https://i.imgur.com/PBHO2wF.png">
4. You should now see your project folder populated with *selenium_python.py* file.


### Configuration

To configure our script for proxy authentication you will need to define required values.

```
HOSTNAME = ''
PORT = ''
DRIVER = ''
DRIVER_PATH = ''
```

You can get information for `HOSTNAME` and `PORT` on our [users dashboard pannel](https://dashboard.smartproxy.com/).

The configuration guidelines for `DRIVER` and `DRIVER_PATH` can be found in the code itself.

<img src="https://i.imgur.com/JrexozP.png">

### Usage

To start using our proxy configuration script for Selenium you will need to import the `get_driver_settings` and `smartproxy` from `selenium_python` package.

```
from selenium_python import get_driver_settings, smartproxy
```

If you selected a different name for `selenium_python.py` file, make sure to change it when importing as well.

To call the function for proxy authentication simply use `smartproxy()`

Note that Chrome and Firefox has different attributes for that, thus your requests should look along these lines:

*Firefox*

```
browser = webdriver.Firefox(executable_path=r'PATH', proxy=smartproxy())
```

*Chrome*

```
browser = webdriver.Chrome(executable_path=r'PATH', desired_capabilities=smartproxy())
```

*Optional*

Our `selenium_python.py` file comes with `get_driver_settings()` function which will return you an array of options which you have setup in the `selenium_python()` file itself for DRIVER settings.

The following variables are available in the returned array:

```
DRIVER_SETTINGS['DRIVER']
DRIVER_SETTINGS['DRIVER_PATH']
```

*Make sure to assign them to another variable when calling the function itself*

### Testing

If you want to run a quick test with our proxy configuration, you can download our `example.py` file using the following command:

```
curl https://raw.githubusercontent.com/Smartproxy/Selenium/master/python/example.py > example.py
```
<img src="https://content.screencast.com/users/JohanSP/folders/Jing/media/3c5a26dc-839a-4882-a47e-dce85fbb0358/smartproxy-selenium-python-code-sample-github-curl.png">
In order to run it, simply execute `python example.py` command while in your project directory.
<img src="https://i.imgur.com/BFzywfC.png">
*Note that the `example.py` file should be in the same directory as `selenium_python.py` file.*

## Need help?
Email - sales@smartproxy.com
<br><a href="https://smartproxy.com">Live chat 24/7</a>
<br><a href="https://join.skype.com/invite/bZDHw4NZg2G9">Skype</a>
<br><a href="https://t.me/smartproxy_com">Telegram</a>
