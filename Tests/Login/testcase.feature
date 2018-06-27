Feature: verifications for the top menu

@smoke
Scenario: Verify every link in the menu on big desktop size
    And I am on "/"
    # And I click the "Portfolio" link ### Maybe this fails becausethe link text says more than Portfolio
    And I click id"login-link"
    Then I should be taken to "/user/"
