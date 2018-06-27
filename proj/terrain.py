import sys
import os
from lettuce import world, before, after, step, steps
from selenium import webdriver
from libs import builtins


# Configuration section
# TODO: this will be done elsewhere


def get_platform():
    platforms = {
        'linux1': 'Linux',
        'linux2': 'Linux',
        'win32': 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform

    return platforms[sys.platform]


PLATFORM = get_platform()

# Select urls based off of environment.
for e in builtins.URL_FOR_ENV.keys():
    if e in sys.argv:
        world.server_url = builtins.URL_FOR_ENV[e]
        break
else:
    raise ValueError("Environment is not vailable")


# Selects browser size based off of argument
for b in builtins.BROWSER_SIZE:
    if b in sys.argv:
        b_size = builtins.BROWSER_SIZE[b]
        break
else:
    b_size = builtins.BROWSER_SIZE["-t-default"]
world.browser_width, world.browser_height = b_size



@before.all  # Do this before all tests are run.
def setUpClass():
    """ Establishes the driver in which the tests will be run.
        NOTE: Right now only chrome options are available in each IOS  
    """

    if builtins.VIRTUAL_DISPLAY:
        from pyvirtualdisplay import Display
        display = Display(visible=0, size=(world.browser_width, world.browser_height))
        display.start()

    if PLATFORM == 'Windows':
        raise ValueError("tool has not  {} not implemented yet".format(PLATFORM))
    elif PLATFORM == 'Linux':
        if builtins.BROWSER == "chrome":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--xvfb')
            chrome_options.add_argument(
                "--window-size={},{}".format(world.browser_width, world.browser_height))
            world.driver = webdriver.Chrome(os.path.join(
                os.path.curdir, "drivers/chromedriver"), options=chrome_options)
        
        # elif builtins.BROWSER == "firefox":
        #     world.driver = webdriver.Firefox(
        #         executable_path="drivers\geckodriver.exe")
        # elif builtins.BROWSER == "edge":
        #     world.driver = webdriver.Edge("drivers\MicrosoftWebDriver.exe")
        # elif builtins.BROWSER == "ie":
        #     world.driver = webdriver.Ie("drivers\IEDriverServer.exe")
        # elif builtins.BROWSER == "pjs":
        #     world.driver = webdriver.PhantomJS(
        #         service_log_path='Lettuce\drivers\ghostdriver.log')
        else:
            ValueError("Browser {} not implemented yet".format(builtins.BROWSER))
    else:
        raise ValueError("IOS {} not implemented yet".format(PLATFORM))


@after.all  # Do this after all tests have ran.
def tearDownClass(total):
    total = world
    total.driver.quit()