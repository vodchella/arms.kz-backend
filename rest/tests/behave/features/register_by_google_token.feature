Feature: Register with Google Auth token

  Scenario: Don't specify token
      Given I try to register without token
       Then I will get "422" http error with "-32001" application error

  Scenario: Specify invalid token
      Given I try to specify invalid Google Auth token
       Then I will get "400" http error with "-32002" application error