Feature: Basic Tests

Scenario Outline: Test Header Links
  Given I am on "/"
  When I click the xpath "<xpath>"
  Then I should be taken to "<url>"

Examples:
| xpath | url |
| //*[@id='leagues']/a | /leagues |
| //*[@id='about']/a | /about |
| //*[@id='rules']/a | /rulesandregulations |
| //*[@id='shop']/a | /shop |
| //*[@id='block-system-main-menu']/ul/li[6]/a | /roundup |
| //*[@id='login-link']/a | /user |
