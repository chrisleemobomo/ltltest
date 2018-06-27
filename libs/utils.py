
from proj.terrain import world
import time
from libs import consts

#-------------------------------------------------------------- VERIFICATIONS


def verify_url_is_present(url):
    """ Verifies given URL is present"""
    return url in world.driver.current_url

#---------------------------------------------------------------------- WAITS


def wait_seconds(seconds):
    """ Waits for the given amount of seconds"""
    time.sleep(seconds)


def wait_for_page_to_load(tries=10, interval=0.2):
    """ Waits for the page to load"""
    for _ in range(tries):
        if world.driver.execute_script('return document.readyState;') != 'complete':
            time.sleep(interval)
        else:
            break
    else:
        raise ValueError("URL failed to load in the given time")

#--------------------------------------------------------------- FIND ELEMENT/S


def find_element(idtype, value, element=None):
    """ finds an element of idtype with value id """
    if element is None:
        element = world.driver
    search_function = getattr(element, consts.SEARCH_TYPES[idtype])
    return search_function(value)


def find_elements(idtype, value, element=None):
    """ finds all elements of idtype with value value. returns a list"""
    if element is None:
        element = world.driver
    if idtype == "id":
        return [find_element(idtype, value, element)]
    search_function = getattr(element, consts.MULTIPLE_SEARCH_TYPES[idtype])
    return search_function(value)

#--------------------------------------------------------------- MAIL HARVESTING METHODS


def get_last_verification_code():
    """ Logs in to gmail account using imap and retrieves the security code from the last mail received.
    """
    import imaplib
    import email
    import re

    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(consts.EMAIL_ACCOUNT, consts.PASSWORD)
    mail.list()
    mail.select('inbox')
    _, data = mail.uid('search', None, "UNSEEN")
    x = len(data[0].split()) - 1  # x is the id of the last mail recieved

    latest_email_uid = data[0].split()[x]
    _, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
    raw_email = email_data[0][1]
    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)

    # Body details
    for part in email_message.walk():
        if part.get_content_type() == "text/html":
            body = part.get_payload(decode=True)
            obtained = re.search("USE THIS CODE: ([0-9]{6})", body)
            return obtained.group(1)
    raise ValueError("Failed to find the verification code in the mail")
