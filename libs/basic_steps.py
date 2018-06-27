from libs import utils, consts
import time
from proj.terrain import steps, step, world
from selenium.common.exceptions import NoSuchElementException


@steps
class NavigationSteps(object):
    """ This class is in charge of URL changes and site navigation
    """

    @step(u'I am on "([^"]*)"')
    def i_am_on_url(step, url):
        """ Make the driver go to the given URL and verify it could be reached:

            >>> Given I am on "/home"

        """
        world.driver.get(world.server_url + str(url))
        if not utils.verify_url_is_present(url):
            raise ValueError("could not reach {}".format (url))

    @step(u'I should be taken to "([^"]*)"')
    def then_i_should_be_taken_to_url(step, url):
        """ Waits for the page to load and then verifies it:

            >>> Then I should be taken to "/home"

        """
        utils.wait_for_page_to_load(5, 0.3)
        utils.verify_url_is_present(url)

    @step(u'I click the "([^"]*)" link')
    def when_i_click_the_link_text_link(step, link_text):
        """ clicks on line given link:

            >>> And I click the "Forgot Password?" link

        """
        world.driver.find_element_by_link_text(str(link_text)).click()

    @step(u'I wait "([^"]*)" seconds')
    def and_i_wait_seconds(step, seconds):
        """ Waits for the given amount of seconds:

            >>> And I wait "0.5" seconds

        """
        time.sleep(float(seconds))

    @step(u'_ And I halt')
    def and_i_wait_seconds(step):
        """ Waits for the given amount of seconds:

            >>> And I wait "0.5" seconds

        """
        while True:
            time.sleep(3)

    @step(u'the "([^"]*)" link is present')
    def and_the_link_with_text_is_present(step, link_text):
        """ Verifies the link_with_given_text is presen:

            >>> And the "Forgot Password?" link is present

        """
        world.driver.find_element_by_link_text(link_text)

    @step(u'I am on a device of "([^"]*)" by "([^"]*)"')
    def i_am_on_a_mobile(step,width,height):
        """ Make the browser change its width and height in pixels

            >>> Given I am on a device of "500" by "700"

        """
        world.browser_width, world.browser_height = [width,height]
        world.driver.set_window_size(width,height)

    @step(u'I scroll down to the bottom of page')
    def scroll_to_bottom_of_page(step):
        time.sleep(1)
        step = 100
        height = world.driver.execute_script(
            "return document.body.scrollHeight") / 2
        for i in range(0, height, step):
            world.driver.execute_script("window.scrollTo(0,{})".format(i))
        else:
            world.driver.execute_script(
                "window.scrollTo(0,document.body.scrollHeight)")



@steps
class BasicObjectStepts(object):

    @step(u'I click the "([^"]*)" button')
    @step(u'I click the button with text "([^"]*)"')
    def i_click_the_button_with_text(step, button_text):
        """ Finds and clicks the button with the given text 

            >>> And I click the "clickableObject" button
            or
            >>> And I click the button with text "goButton"

        """
        world.driver.find_element_by_xpath(
            "//button[contains(text(),'%s')]" % button_text).click()
        utils.wait_seconds(0.5)

    @step(u'I click {}"([^"]*)"'.format(consts.SELECTOR_TYPES))
    @step(u'I click the {}"([^"]*)" button'.format(consts.SELECTOR_TYPES))
    def and_i_click_the_button_with_xpath(step, idtype, i):
        """ Finds and clicks the button/object:

            >>> And I click id"clickableObject"
            or
            >>> And I click the id"goButton"

        """
        utils.find_element(idtype, i).click()
        utils.wait_seconds(0.5)

#--------------------------------------------------------- OBJ IS/IS NOT PRESENT

    @step(u'the {}"([^"]*)" object is present'.format(consts.SELECTOR_TYPES))
    def the_object_is_present(step, idtype, i):
        """ Verifies the object is present:

            >>> And the id"userName" object is present

        """
        utils.find_element(idtype, i)

    @step(u'the {}"([^"]*)" object is not present'.format(consts.SELECTOR_TYPES))
    def the_object_is_not_present(step, idtype, i):
        """ Verifies the object is not present:

            >>> And the id"userName" object is not present

        """
        try:
            element = utils.find_element(idtype, i)
        except NoSuchElementException:
            # The element is indeed not present
            pass
        else:
            raise ValueError("Element is present when it should not be %s" % str(
                element))

#--------------------------------------------------------------- FILL CONTAINERS

    @step(u'I fill in {}"([^"]*)" with "([^"]*)"'.format(consts.SELECTOR_TYPES))
    def i_fill_in_object_with_content(step, idtype, i, text):
        """ Finds and fills up the object with the given text:

            >>> And I fill in id"userName" with "test@test.com"

        """
        utils.find_element(idtype, i).send_keys(text)

#----------------------------------------------------- ELEMENT IS WITHIN ELEMENT

    @step(u'{0}"([^"]*)" contains {0}"([^"]*)"'.format(consts.SELECTOR_TYPES))
    def object_contains_object(step, type_id_f, id_f, type_id_c, id_c):
        """ finds the father element and then checks the element contains a 
            second (child) element:

            >>> cn"forgot-password" contains lt"Forgot Password?"

        """
        element = utils.find_element(type_id_f, id_f)
        utils.find_element(type_id_c, id_c, element)

#-------------------------------------------------- CLICK ELEMENT WITHIN ELEMENT

    @step(u'I click the {0}"([^"]*)" object inside the {0}"([^"]*)" object'.format(consts.SELECTOR_TYPES))
    def object_contains_object(step, type_id_c, id_c, type_id_f, id_f):
        """ finds the father element and then checks the element contains a 
            second (child) element:

            >>> cn"forgot-password" contains lt"Forgot Password?"

        """
        element = utils.find_element(type_id_f, id_f)
        utils.find_element(type_id_c, id_c, element).click()

#-------------------------------------------------------------- ELEMENT CONTAINS

    @step(u'{0}"([^"]*)" contains the text "([^"]*)"'.format(consts.SELECTOR_TYPES))
    def object_contains_object(step, idtype, id, text):
        """ Checks the given element contains the given text:

            >>> cn"forgot-password" contains the text "Forgot Password?"

        """
        element = utils.find_element(idtype, id)
        if text not in element.text:
            raise ValueError("{} not in {}".format(text, element.text))

    @step(u'{0}"([^"]*)" has class "([^"]*)"'.format(consts.SELECTOR_TYPES))
    def object_has_class(step, idtype, id, class_name):
        """ Checks the given element has the given class:

            >>> And id"header" has class "wow fadeInDown active"

        """
        element = utils.find_element(idtype, id)
        classes = element.get_attribute("class")
        if classes != class_name:
            raise ValueError('The "{0}" element does not have class "{1}"; the {0} element has class "{2}"'.format(id, class_name, classes))

#-------------------------------------------------------------- CLEAR CONTAINERS

    @step(u'I erase {}"([^"]*)"'.format(consts.SELECTOR_TYPES))
    def I_erase_the_object(step, idtype, i):
        """ Erases the given object's content:

            >>> And I erase id"userName"

        """
        utils.find_element(idtype, i).clear()
