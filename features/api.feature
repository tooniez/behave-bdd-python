Feature: API Response Testing
  As a developer
  I want to test a free API response
  So that I can ensure it returns the expected data

  Scenario: Validate API response
    Given I make a request to the free API
    When I receive the response
    Then the response status should be 200
