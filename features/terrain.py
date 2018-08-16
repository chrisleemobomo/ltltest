import sys
import random
import unittest
from lettuce import *
from nose.tools import *
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from platforms.ios import PlatformIOS
#from platforms.android import PlatformAndroid

# Select urls based off of environment.
if "-t-local" in sys.argv:
    world.server_url = "http://127.0.0.1:8080"
elif "-t-dev" in sys.argv:
    world.server_url = "localhost"
elif "-t-stage" in sys.argv:
    world.server_url = "localhost"
elif "-t-prod" in sys.argv:
    world.server_url = "https://www.localtennisleagues.com"
elif "-t-test" in sys.argv:
    world.server_url = "https://www.localtennisleagues.com"
elif "-t-appium" in sys.argv:
    world.server_url = "http://0.0.0.0:4723"
else:
    world.server_url = "https://www.localtennisleagues.com"

# Selects browser size based off of argument
if "-t-iphone" in sys.argv:
    browser_width = 750
    browser_height = 1334
elif "-t-nexus" in sys.argv:
    browser_width = 1080
    browser_height = 1920
elif "-t-ipad" in sys.argv:
    browser_width = 1536
    browser_height = 2048
else:
    browser_width = 1920
    browser_height = 1080


# Common Pages
    world.login = world.server_url + "/login"


@before.all  # Do this before all tests are ran.
def setUpClass():
    world.driver = None
    if "-t-chrome" in sys.argv:
        #world.driver = webdriver.Chrome("/Users/chrislee/lettuce/drivers/chromedriver237")
        world.driver = webdriver.Chrome("/home/chris/chromedriver")
    elif "-t-firefox" in sys.argv:
        world.driver = webdriver.Firefox(executable_path="/Users/chrislee/lettuce/drivers/geckodriver")
    elif "-t-phantomjs" in sys.argv:
        world.driver = webdriver.PhantomJS(
            service_log_path='/Users/chrislee/lettuce/drivers/ghostdriver.log')
    elif "-t-chromeheadless" in sys.argv:
       options = Options()
       options.add_argument('--headless')
       options.add_argument('--disable-gpu')  # Last I checked this was necessary.
       world.driver = webdriver.Chrome('/home/chris/chromedriver', chrome_options=options)
    elif "--tag=ios" in sys.argv:
        platform_ios = PlatformIOS()
        world.driver = platform_ios.driver()
        world.translator = platform_ios.id_translator
    elif "--tag=android" in sys.argv:
        platform_android = PlatformAndroid()
        world.driver = platform_android.driver()
        world.translator = platform_android.id_translator
    else:
       options = Options()
       options.add_argument('--headless')
       options.add_argument('--disable-gpu')  # Last I checked this was necessary.
       world.driver = webdriver.Chrome('/home/chris/chromedriver', chrome_options=options)
       #world.driver = webdriver.Chrome('/Users/chrislee/lettuce/drivers/chromedriver237', chrome_options=options)

    world.driver.set_window_size(browser_width, browser_height)


@after.all  # Do this after all tests have ran.
def tearDownClass(total):
    total = world
    total.driver.quit()
