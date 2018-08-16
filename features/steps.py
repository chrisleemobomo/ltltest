#  coding=utf-8
from terrain import *
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time

@steps
class Steps(object):

    @step(u'Then the title of the page should become "([^"]*)"')
    def the_title_of_the_page_should_become(step, result):
        title = world.driver.title
        try:
            assert_true(step, title == result)
        except AssertionError as e:
            world.driver.quit()

    # @step(u'when I fill in "([^"]*)" with "([^"]*)"')
    # def when_i_fill_in(step, locator, username):
    #     try:
    #         world.browser.find_element_by_name(locator).sendkeys(username)
    #     except AssertionError as e:
    #         world.browser.quit()
    #
    # @step(u'When I click "([^"]*)"')
    # def when_i_press(step, locator):
    #     try:
    #         world.browser.find_element_by_link_text(locator).click()
    #     except AssertionError as e:
    #         world.browser.quit()

    @step(u'Then the browser should close')
    def then_the_browser_should_close(step):
        world.driver.quit()

    @step(u'When I click the xpath "([^"]*)"')
    def when_i_click_the_xpath_group1(step, group1):
        world.driver.find_element_by_xpath(str(group1)).click()


    @step(u'Given I am on "([^"]*)"')
    def given_i_am_on_group1(step, group1):
        world.driver.get(world.server_url + str(group1))

    @step(u'Then I should be taken to "([^"]*)"')
    def then_i_should_be_taken_to_group1(step, group1):
        assert(group1 in world.driver.current_url)

    @step(u'When I fill in the search field with "([^"]*)"')
    def when_i_fill_in_the_search_field_with_group1(step, group1):
        time.sleep(2)
        world.driver.find_element_by_xpath('/html/body/header/div[3]/nav/div[2]/div[1]/div/div/div/input').send_keys(str(group1))
        time.sleep(1)

    @step(u'Then I should see results')
    def then_i_should_see_results(step):
        world.driver.find_element_by_xpath('//*[text()="PRS McCarty 594 Trampas Green 10 Top w/ Case"]')
        time.sleep(2)

    @step(u'When I fill in forgot password email with "([^"]*)"')
    def when_i_fill_in_forgot_password_email_with_group1(step, group1):
        world.driver.find_element_by_id("userName").send_keys(str(group1))
        world.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/form/div[2]/h1').click()
        time.sleep(2)

    @step(u'When I fill in DOB with "([^"]*)"')
    def when_i_fill_in_dob_with_group1(step, group1):
        time.sleep(2)
        #world.driver.find_element_by_xpath('//*[text()="Reset Password"]')
        #world.driver.find_element_by_xpath('//*[text()="SECURITY QUESTION"]')
        #world.driver.find_element_by_xpath('//*[text()="What is your Date of Birth?"]')
        world.driver.find_element_by_id("securityAnswer").send_keys(str(group1))
        time.sleep(2)

    @step(u'And I click the Submit button')
    def and_i_click_the_sign_in_button(step):
        world.driver.find_element_by_xpath("/html/body/header/div[3]/nav/div[2]/div[1]/div/div/div/a").click()
        time.sleep(2)

    @step(u'Then I should see the forgot password confirmation')
    def then_i_should_see_the_forgot_password_confirmation(step):
        world.driver.find_element_by_xpath('//*[text()="Reset Password"]')
        world.driver.find_element_by_xpath('//*[text()="CHECK YOUR E-MAIL"]')
        world.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/form/div[2]/div/div/div[1]/span')
        world.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/form/div[2]/div/div/div[2]')
        world.driver.find_element_by_link_text('dcrb.selfservice@dc.gov')
        time.sleep(2)

    @step(u'Then I should see the User Not Registered message')
    def then_i_should_see_the_user_not_registered_message(step):
        time.sleep(1)
        world.driver.find_element_by_xpath('//*[text()="User not registered."]')
        time.sleep(2)

    @step(u'Then I should see an Invalid Date message')
    def then_i_should_see_an_invalid_date_message(step):
        world.driver.find_element_by_xpath('//*[text()="Invalid date."]')
        time.sleep(2)

    @step(u'When I erase the DOB')
    def when_i_erase_the_dob(step):
        world.driver.find_element_by_id("securityAnswer").clear()
        time.sleep(1)
















    @step(u'When I can log in using "([^"]*)" and "([^"]*)"')
    def when_can_log_in_using_and(step, group1, group2):
        time.sleep(5)
        world.driver.find_element_by_id("userName").send_keys(str(group1))
        world.driver.find_element_by_id("password").send_keys(str(group2))
        world.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/form/div[2]/div/div[5]/div[2]/button").click()
        time.sleep(30)

    @step(u'And I click the Continue button')
    def and_i_click_the_continue_button(step):
        world.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/form/div[2]/div/div/div[3]/div[2]/button").click()
        time.sleep(5)

    @step(u'And I wait thirty seconds')
    def and_i_wait_thirty_seconds(step):
        world.driver.find_element_by_id("code").clear()
        time.sleep(30)

    @step(u'And the Forgot Password link is present')
    def and_the_forgot_password_link_is_present(step):
        world.driver.find_element_by_link_text("Forgot Password?")
        time.sleep(2)

    @step(u'When I click the "([^"]*)" link')
    def when_i_click_the_group1_link(step, group1):
        time.sleep(1)
        world.driver.find_element_by_link_text(str(group1)).click()
        time.sleep(2)

    @step(u'And the Disclaimer is present')
    def and_the_disclaimer_is_present(step):
        world.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/form/div[2]/div/div[6]')

    @step(u'And I click the Go button')
    def and_i_click_the_go_button(step):
        world.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/form/div[2]/div/div[5]/div[2]/button").click()
        time.sleep(2)

    @step(u'Then I should see "([^"]*)"')
    def then_i_should_see_group1(step, group1):
        world.driver.find_element_by_xpath("//*[text()=''str(group1)'']")
        time.sleep(2)

    @step(u'And the Login and Password fields are present')
    def and_the_login_and_password_fields_are_present(step):
        world.driver.find_element_by_id("userName")
        world.driver.find_element_by_id("password")

    @step(u'And the Sign Up and Go buttons are present')
    def and_the_sign_up_and_go_buttons_are_present(step):
        world.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/form/div[2]/div/div[5]/div[1]/a')
        world.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/form/div[2]/div/div[5]/div[2]/button')

    @step(u'And the verification field is present')
    def and_the_verification_field_is_present(step):
        world.driver.find_element_by_id("code")

    @step(u'And the Back and Submit buttons are present')
    def and_the_back_and_submit_buttons_are_present(step):
        world.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/form/div[2]/div/div/div[3]/div[1]/a')
        world.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/form/div[2]/div/div/div[3]/div[2]/button')

    @step(u'When I fill in email with "([^"]*)"')
    def when_i_fill_in_email_with_group1(step, group1):
        world.driver.find_element_by_id("userName").send_keys(str(group1))
        world.driver.find_element_by_id("password").click
        time.sleep(2)

    @step(u'When I fill in password with "([^"]*)"')
    def when_i_fill_in_password_with_group1(step, group1):
        world.driver.find_element_by_id("password").send_keys(str(group1))
        world.driver.find_element_by_id("userName").click
        time.sleep(2)

    @step(u'When I erase the password')
    def when_i_erase_the_password(step):
        world.driver.find_element_by_id("password").clear()
        time.sleep(1)

    @step(u'When I erase the email')
    def when_i_erase_the_email(step):
        world.driver.find_element_by_id("userName").clear()
        time.sleep(1)

    @step(u'Then I should see the Required Email message')
    def then_i_should_see_the_required_email_message(step):
        world.driver.find_element_by_xpath('//*[text()="This is required."]')
        time.sleep(2)

    @step(u'When I fill in the verification code with "([^"]*)"')
    def when_i_fill_in_the_verification_code_with_group1(step, group1):
        time.sleep(5)
        world.driver.find_element_by_id("code").send_keys(str(group1))
        time.sleep(2)

    @step(u'Then I should see an Invalid Email message')
    def then_i_should_see_an_invalid_email_message(step):
        world.driver.find_element_by_xpath('//*[text()="Invalid E-Mail."]')
        time.sleep(2)

    @step(u'Then I should see the Invalid Login message')
    def then_i_should_see_an_invalid_login_message(step):
        world.driver.find_element_by_id('snackbar-container')
        world.driver.find_element_by_xpath('//*[text()="Invalid user name and/or password."]')
        time.sleep(2)

    @step(u'Then I should see the Invalid Code message')
    def then_i_should_see_an_invalid_code_message(step):
        time.sleep(3)
        world.driver.find_element_by_id('snackbar-container')
        world.driver.find_element_by_xpath('//*[text()="The verification code is invalid."]')
        time.sleep(2)

    @step(u'Then I should see a Password required message')
    def then_i_should_see_a_password_required_message(step):
        world.driver.find_element_by_xpath('//*[text()="This is required."]')
        time.sleep(2)

    @step(u'Then I should see the Unconfirmed Email message')
    def then_i_should_see_the_unconfirmed_email_message(step):
        world.driver.find_element_by_id('snackbar-container')
        world.driver.find_element_by_xpath('//*[text()="E-Mail is not confirmed."]')
        time.sleep(2)

    @step(u'Then I should see Locked Out message')
    def then_i_should_see_the_locked_out_message(step):
        world.driver.find_element_by_id('snackbar-container')
        world.driver.find_element_by_xpath('//*[text()="The user is locked out. Try again later or reset your password."]')
        time.sleep(2)

    @step(u'And I click the Go button')
    def and_i_click_the_go_button(step):
        world.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/form/div[2]/div/div[3]/div/button[2]").click()

    @step(u'And I click the verification submit button')
    def and_i_click_the_verification_submit_button(step):
        world.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/form/div[2]/div/div/div[3]/div[2]/button").click()

    @step(u'And I click the Sign In button')
    def and_i_click_the_sign_in_button(step):
        world.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/form/div[2]/div/div[5]/div[2]/button").click()
        time.sleep(2)

    @step(u'And I click the Next button')
    def and_i_click_the_next_button(step):
        world.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/form/div[2]/div/div[3]/div/button[2]").click()

    @step(u'Then I should be taken to "([^"]*)"')
    def then_i_should_be_taken_to_group1(step, group1):
        comparison_url = world.server_url + str(group1)
        assert_equals(world.driver.current_url, comparison_url)

    @step(u'And I should not see ')
    def and_i_should_not_see_the_message(step):
        try:
            time.sleep(1)
            world.driver.find_element_by_xpath('//*[text()="This is a District of Columbia Retirement Board computer system, and may be accessed only by authorized users. Unauthorized access or use, may subject violators to criminal and/or civil action."]')
            time.sleep(3)
            assert False, "Test works"
        except NoSuchElementException:
            assert True, "Test doesn't work"



















    @step(u'And I click the Sign Up button')
    def and_i_click_the_sign_up_button(step):
        world.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/form/div[2]/div/div[5]/div[1]/a").click()
        time.sleep(2)

    @step(u'And I click the Reg Next button')
    def and_i_click_the_reg_next_button(step):
        world.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div[2]/button").click()

    @step(u'And I click the Reg Submit button')
    def and_i_click_the_reg_submit_button(step):
        world.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/form/div[2]/div/div/div[4]/div[2]/button").click()

    @step(u'And I see the App Store buttons')
    def and_i_see_the_app_store_buttons(step):
        world.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/form/div[4]/span[2]/a[1]")
        world.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/form/div[4]/span[2]/a[2]")
        world.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div[1]/button")
        time.sleep(2)

    @step(u'When I fill in ssn with "([^"]*)"')
    def when_i_fill_in_ssn_with_group1(step, group1):
        world.driver.find_element_by_id("ssn").send_keys(str(group1))
        world.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/form/div[2]/h1').click()
        time.sleep(2)

    @step(u'When I fill in birthdate with "([^"]*)"')
    def when_i_fill_in_birthdate_with_group1(step, group1):
        world.driver.find_element_by_id("birthDate").send_keys(str(group1))
        world.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/form/div[2]/h1').click()
        time.sleep(2)

    @step(u'When I fill in first name with "([^"]*)"')
    def when_i_fill_in_first_name_with_group1(step, group1):
        world.driver.find_element_by_id("firstName").send_keys(str(group1))
        world.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/form/div[2]/h1').click()
        time.sleep(2)

    @step(u'When I fill in last name with "([^"]*)"')
    def when_i_fill_in_last_name_with_group1(step, group1):
        world.driver.find_element_by_id("lastName").send_keys(str(group1))
        world.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/form/div[2]/h1').click()
        time.sleep(2)

    @step(u'When I fill in reg email with "([^"]*)"')
    def when_i_fill_in_reg_email_with_group1(step, group1):
        world.driver.find_element_by_id("email").send_keys(str(group1))
        world.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/form/div[2]/h1').click()
        time.sleep(2)

    @step(u'When I fill in phone with "([^"]*)"')
    def when_i_fill_in_phone_with_group1(step, group1):
        world.driver.find_element_by_id("phoneNumber").send_keys(str(group1))
        world.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/form/div[2]/h1').click()
        time.sleep(2)

    @step(u'When I fill in password1 with "([^"]*)"')
    def when_i_fill_in_password1_with_group1(step, group1):
        world.driver.find_element_by_id("password").send_keys(str(group1))
        world.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/form/div[2]/h1').click()
        time.sleep(2)

    @step(u'When I fill in password2 with "([^"]*)"')
    def when_i_fill_in_password2_with_group1(step, group1):
        world.driver.find_element_by_id("confirmPassword").send_keys(str(group1))
        world.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/form/div[2]/h1').click()
        time.sleep(2)

    @step(u'When I erase the ssn')
    def when_i_erase_the_ssn(step):
        world.driver.find_element_by_id("ssn").clear()
        time.sleep(1)

    @step(u'When I erase the birthdate')
    def when_i_erase_the_birthdate(step):
        world.driver.find_element_by_id("birthDate").clear()
        time.sleep(1)

    @step(u'When I erase the first name')
    def when_i_erase_the_first_name(step):
        world.driver.find_element_by_id("firstName").clear()
        time.sleep(1)

    @step(u'When I erase the last name')
    def when_i_erase_the_last_name(step):
        world.driver.find_element_by_id("lastName").clear()
        time.sleep(1)

    @step(u'When I erase the reg email')
    def when_i_erase_the_reg_email(step):
        world.driver.find_element_by_id("email").clear()
        time.sleep(1)

    @step(u'When I erase the phone')
    def when_i_erase_the_phone(step):
        world.driver.find_element_by_id("phoneNumber").clear()
        time.sleep(1)

    @step(u'When I erase the password2')
    def when_i_erase_the_password2(step):
        world.driver.find_element_by_id("confirmPassword").clear()
        time.sleep(1)

    @step(u'Then I should see an Invalid SSN message')
    def then_i_should_see_an_invalid_ssn_message(step):
        world.driver.find_element_by_xpath('//*[text()="Please enter a valid SSN."]')
        time.sleep(2)

    @step(u'Then I should see an Invalid Birthdate message')
    def then_i_should_see_an_invalid_birthdate_message(step):
        world.driver.find_element_by_xpath('//*[text()="Invalid date."]')
        time.sleep(2)

    @step(u'Then I should see the Email Already In Use Message')
    def then_i_should_see_the_email_already_in_use_message(step):
        world.driver.find_element_by_xpath('//*[@id="snackbar1506449940282"]/span/span[1]')
        time.sleep(2)

    @step(u'Then I should see the Passwords Do Not Match Message')
    def then_i_should_see_the_passwords_do_not_match_message(step):
        world.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div/div[4]/div/div')
        time.sleep(2)

    @step(u'And I see the password rules')
    def and_i_see_the_password_rules(step):
        world.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div/password-validation/ul/li[1]')
        world.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div/password-validation/ul/li[2]')
        world.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div/password-validation/ul/li[3]')
        time.sleep(2)

    @step(u'And I see the terms of service')
    def and_i_see_the_terms_of_service(step):
        time.sleep(2)
        world.driver.find_element_by_xpath('//*[text()="Sign Up"]')
        #world.driver.find_element_by_xpath('//*[text()="TERMS AND CONDITIONS"]')
        world.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/form/div[2]/div/h2')
        world.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/form/div[2]/div/div/div[1]')
        world.driver.find_element_by_xpath('//*[text()="I ACCEPT TERMS AND CONDITIONS"]')
        world.driver.find_element_by_id('termsAndConditions')
        time.sleep(2)

    @step(u'And I accept the terms of service')
    def and_i_accept_the_terms_of_service(step):
        world.driver.find_element_by_id('termsAndConditions').click()
        time.sleep(2)

    @step(u'Then I should see the registration confirmation')
    def then_i_should_see_the_registration_confirmation(step):
        time.sleep(2)
        world.driver.find_element_by_xpath('//*[text()="Sign Up"]')
        world.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/form/div[2]/div/h2')
        world.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/form/div[2]/div/div/div[2]')
        world.driver.find_element_by_partial_link_text('dcrb.selfservice@dc.gov')
        time.sleep(2)
