from proj.terrain import steps, step, world
from libs.basic_steps import NavigationSteps
import proj.preconditions
from libs import utils


@steps
class SpecificNavigationSteps(NavigationSteps):
    """ This class is in charge of specific URL changes and site navigation
    """

    @step(u'I am on "([^"]*)"')
    def i_am_on_url(step, url):
        """ Make the driver go to the given URL and verify it could be reached:

            >>> Given I am on "/home"

        """
        world.driver.get(world.server_url + str(url))


        # if the QA environment redirects you to wp-login 
        # then you need to log in with the following steps
        
        if utils.verify_url_is_present("/wp-login"):
            utils.wait_for_page_to_load()
            step.behave_as("""
              And I fill in cn"input" with "qa-tests"
              And I fill in id"user_pass" with "Ius7poVE1clut63cljcWxqS*"
              And I click id"wp-submit"
              """)
            utils.wait_for_page_to_load()
            world.driver.get(world.server_url + str(url))
        if not utils.verify_url_is_present(url):
            raise ValueError("could not reach {}".format (url))



