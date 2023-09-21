Feature: Outbound Call Actions
    As an agent,
    I want to be able to perform actions during the call

    Background:
        Given "agent" is logged in to the phone
        And "agent" is on "keyboard" page
        And "client" can accept calls # for automation we'll use another client. For manual testing it can be cellular number as well

    @critical
    Scenario: Agent may give a call to a client and client may accept it
        When "agent" calls to "client"
        Then "client" should see "agent" ringing

        When "client" accepts call
        Then "agent" should hear "client" speaking
        And "client" should hear "agent" speeking

    @critical
    Scenario: Agent may give a call to a client and client may decline it
        When "agent" calls to "client"
        Then "client" should see "agent" ringing

        When "client" declines call
        Then "agent" should not hear "client" speaking
        # and probably sees something
        And "client" should not hear "agent" speeking
    # and probably sees something

    @critical
    Scenario: Agent can drop the call
        Given: "agent" has a call with "client"
        When "agent" drops the call
        Then "client" should not hear "agent" speaking
        # and probably sees something
        And "client" should not hear "agent" speaking
    # and probably sees something

    @major
    Scenario: The call should be terminated when client drops the call
        Given: "agent" has a call with "client"
        When "client" drops the call
        Then "agent" should not hear "client" speaking
        # and probably sees something
        And "client" should not hear "agent" speaking
    # and probably sees something

    @major
    Scenario: Agent hears long signal while waiting
        When "agent" calls to "client"
        Then "agent" hears long signal while waiting for call to be accepted

    @moderate
    Scenario: Agent should see timer showing call duration properly
        Given: "agent" has a call with "client"
        Then "agent" should see timer showing call duration properly

    @major
    Scenario Outline: Agent can not call to invalid number
        When "agent" types "<number>" to the number field
        Then "agent" should hear error message "calling to invalid number"

        Examples:
            | number               |
            | 12                   |
            | 12345678901234567890 |
            | +1111111111          |

    @major
    Scenario Outline: Agent can not call to short or special numbers
        When "agent" types "<number>" to the number field
        Then "agent" should hear error message "caling to short or special numbers is not allowed"

        Examples:
            | number |
            | 911    |
            | *111#  |

    @moderate
    Scenario: Agent may call to contact
        When "agent" calls to "client" by contact name
        Then "client" should see "agent" ringing
        And "agent" should see "client" phone number and name


    @moderate
    Scenario: Agent may call to teammate
        When "agent" calls to "client" by teammate name
        Then "client" should see "agent" ringing
        And "agent" should see "client" phone number and name

    @moderate
    Scenario: Agent sees error message if service is down
        Given: "agent" has a call with "client"
        When service is down
        Then "agent" should see error message "Something went wrong, try again later"
        And "agent" should see link "Contact support"

    @low
    Scenario: Agent can't call himself
        When "agent" calls to "agent"
        Then "agent" should see error message "You can not call yourself"
    # It's funny, but it right now it's possible to call yourself

    @low
    Scenario: Agent's number phone code should be selected by default
        When "agent" cleans the number field
        Then "agent" should see his phone code selected by default

    @low
    Scenario: Agent should see phone code of the country parsed correctly
        When "agent" types "+1" to the number field
        Then "agent" should see phone code of "United States" parsed correctly

        When "agent" clears the number field
        And "agent" types "+34" to the number field
        Then "agent" should see phone code of "Spain" parsed correctly

        Examples:
            | number               |
            | 12                   |
            | 12345678901234567890 |
            | +1111111111          |
