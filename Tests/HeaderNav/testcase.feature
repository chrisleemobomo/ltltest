Feature: Login

@smoke
Scenario: Login
    And I am on "/"
    # And I click the "Portfolio" link ### Maybe this fails becausethe link text says more than Portfolio
    And I click id"leagues"
    Then I should be taken to "/leagues/"
    And I click id"about"
    Then I should be taken to "/about/"
    And I click id"rules"
    Then I should be taken to "/rulesandregulations/"
    And I click id"shop"
    Then I should be taken to "/shop/"
    And I click id"leagues"
    Then I should be taken to "/leagues/"
    And I click xpath"//*[@id='block-system-main-menu']/ul/li[6]/a"
    Then I should be taken to "/roundup"
