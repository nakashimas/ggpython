# -*- coding: utf-8 -*-
# =============================================================================>
# ##############################################################################
# ## 
# ## tracker.py
# ## 
# ##############################################################################
# =============================================================================>
# Definition

CHROME_UPDATE = True

# =============================================================================> 
# imports default
from xml.etree import ElementTree
import urllib.parse
import re
import time
import functools

# =============================================================================> 
# imports third party
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import chromedriver_binary
import chromedriver_autoinstaller as chromedriver

try:
    if CHROME_UPDATE:
        chromedriver.install()
except Exception as e:
    print("ERRR:", e)

# =============================================================================> 
# imports local

# =============================================================================> 
# define local metod

# =============================================================================> 
# define class

class WebsiteAPI(webdriver.Chrome):
    """WebsiteAPI

    Args:
        webdriver.Chrome (_type_): _description_
    References:
        - to solve `--headless timeout`
            https://stackoverflow.com/questions/67744514/timeout-exception-error-on-using-headless-chrome-webdriver
    """
    # =========================================================================>
    # Default
    def __init__(self, *args, **kwargs):
        """ __init__ """
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--ignore-ssl-errors')
        self.options.add_argument('--headless')
        self.options.add_argument('--start-maximized')
        self.options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
        webdriver.Chrome.__init__(self, *args, options = self.options, **kwargs)

        self.set_window_size("12000", "11000")
    
    def __enter__(self):
        """ __enter__ """
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """ __exit__ """
        try:
            self.quit()
        except Exception as e:
            print("_____", "close error")
    
    def __str__(self):
        """ __str__ """
        return "WebsiteAPI"
    
    # =========================================================================>
    # SetGet
    @property
    def options(self):
        """ get options """
        return self.__options
    
    @options.setter
    def options(self, options):
        """ set options """
        if options is None:
            raise TypeError('invalid options')
        self.__options = options

    # =========================================================================>
    # Utils
    def wait_element(self, seconds, element_by = By.CLASS_NAME, target_string = "", timeout = 30):
        wait = WebDriverWait(self, timeout)
        element = wait.until(
            expected_conditions.presence_of_element_located(
                (element_by, target_string)
            )
        )
        time.sleep(seconds)
        return element
    
    def wait_element_clickable(self, seconds, element_by = By.CLASS_NAME, target_string = "", timeout = 30):
        wait = WebDriverWait(self, timeout)
        element = wait.until(
            expected_conditions.element_to_be_clickable(
                (element_by, target_string)
            )
        )
        time.sleep(seconds)
        return element


# =============================================================================> 

if __name__ == "__main__":
    pass
