from proj.terrain import steps, step, world
from libs.basic_steps import BasicObjectStepts
from proj.specific_steps import SpecificNavigationSteps


@steps
class PreconditionSteps(SpecificNavigationSteps, BasicObjectStepts):
    """ This class is in charge of steps related to preconditions
    """

    @step(u'I have logged in and I am in /')
    def log_in(step):
        """ Tries to log in with 'user' and 'psw' credentials and clicks on the 
            button containing the text 'button_text
        """
        step.behave_as("""
        	  Given I am on "/wp-login"
			  And I fill in id"user_login" with "qa-tests"
			  And I fill in id"user_pass" with "Ius7poVE1clut63cljcWxqS*"
			  And I click id"wp-submit"
			  And I wait "1" seconds
			  Then I should be taken to "/"
        	""")