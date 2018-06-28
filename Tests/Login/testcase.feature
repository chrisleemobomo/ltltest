Feature: Login

@smoke
Scenario: Login 
    And I am on "/"
    # And I click the "Portfolio" link ### Maybe this fails becausethe link text says more than Portfolio
    And I click id"login-link"
    Then I should be taken to "/user/"
