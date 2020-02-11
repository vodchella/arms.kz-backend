Feature: View exercise

  Scenario: Do it right
      Given I try to view exercise right
       Then I will get Ok http status

  Scenario: Specify invalid ID
      Given I try to specify invalid exercise ID
       Then I will get "400" http error with "-32001" application error

  Scenario: Specify nonexistent ID
      Given I try to specify nonexistent exercise ID
       Then I will get "400" http error with "-32002" application error
