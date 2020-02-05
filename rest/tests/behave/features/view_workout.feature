Feature: View workout

  Scenario: Do it right
      Given I try to view workout right
       Then I will get Ok http status

  Scenario: Specify invalid ID
      Given I try to specify invalid workout ID
       Then I will get "400" http error with "-32001" application error