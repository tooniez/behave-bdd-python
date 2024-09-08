Feature: Google Search Functionality
  As a user
  I want to search for queries on Google
  So that I can find relevant information quickly

  Scenario: Search for a query on Google
    Given I open the Google webpage
    When I search for "Behave BDD"
    Then I should see results for "Behave BDD"