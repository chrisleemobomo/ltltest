#!/usr/local/bin/python2.7
# encoding: utf-8
"""
This is a library that includes interfaces and basic utils that should be loaded on startup

"""
import os
import sys
import re

# ---------------------------------------------------------------------------DEFAULT VALUES

PROJ_PATH = "."
TESTCASE_TEMPLATE_NAME = 'testcase'
VIRTUAL_DISPLAY = True
VERBOSITY_LEVEL = 3
RECURSIVE = True
DEBUG = False
TESTRUN = False
ENVIRONMENT = 'dev'
DEVICE = "default"
BROWSER = "chrome"


BROWSER_SIZE = {
    "-t-iphone" : [750,1334],
    "-t-nexus" : [1080,1920],
    "-t-ipad" : [1536,2048],
    "-t-default" : [1920,1080],
    "-t-ejemplo" : [1200,780],
}

URL_FOR_ENV = {
    "-t-dev": "http://dev.localtennisleagues.com",
    "-t-staging": "http://staging.localtennisleagues.com",
    "-t-local": "http://127.0.0.1:8080",
    "-t-prod": "https://www.localtennisleagues.com"
}

# --------------------------------------------------------------------------DEFAULT METHODS

def set_up_paths(paths):
    """ Adds the given paths to pythonpath to use up globally
    """
    for p in paths:
        sys.path.append(os.path.join(PROJ_PATH, p))


def get_features_from_path(testpath='Tests'):
    """ Retrns a list of all TESTCASE_TEMPLATE_NAME.feature files within the
            given directory.
            TODO: Ad as well more intermidiate configuration files
    """
    testdirs = []
    for base_dir, folders, files in os.walk(testpath):
        testdirs.extend([os.path.join(base_dir, f) for f in files if re.search(
            TESTCASE_TEMPLATE_NAME, f) and f.endswith('.feature')])
    return testdirs


def print_result(results):
    """ pretty prints results """
    for tc, rc in results:
        print "{}: {} ({})".format("FAIL" if rc else "PASS", tc, rc)


if __name__ == "__main__":
    print get_features_from_path("/qa/dcrb/Tests/Login/ForgotPassword")
