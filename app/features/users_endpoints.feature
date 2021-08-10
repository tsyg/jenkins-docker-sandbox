Feature: Set of endpoints to get information about users

  Scenario: List all users
    Given the following users
      |id|username|
      |1 |user1   |
      |2 |user2   |
      |3 |user3   |
    When I send "GET" request to "/users" endpoint
    Then I should receive the response with "200" status code and the following body
      """
      {
        "success": true,
        "data": [
            {"id": "1", "username": "user1"},
            {"id": "2", "username": "user2"},
            {"id": "3", "username": "user3"}
        ]
      }
      """

  # TODO: As a go through example, create scenario for concrete user endpoint, e.g. /users/1
  # also using data from /users endpoint for integration check between endpoints
