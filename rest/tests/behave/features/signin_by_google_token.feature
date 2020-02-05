Feature: Sign in with Google Auth token

  Scenario: Don't specify token
      Given I try to sign in without token
       Then I will get "400" http error with "-32001" application error

  Scenario: Specify invalid token
      Given I try to sign in with invalid Google Auth token
       Then I will get "400" http error with "-32002" application error