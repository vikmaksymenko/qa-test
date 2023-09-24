Feature: Outbound Calls
    As an caller,
    I want to be able to make outbound calls to customers,
    So that we may have a verbal communication.

    Background:
        Given "caller" is logged in to the phone
        And "caller" is on "keyboard" page
        And "recipient" can accept calls # for automation we'll use another recipient. For manual testing it can be cellular number as well

    @critical
    Scenario: caller may give a call to a recipient and recipient may accept it
        When "caller" calls to "recipient"
        Then "recipient" should see "caller" ringing

        When "recipient" accepts call
        Then "caller" should hear "recipient" speaking
        And "recipient" should hear "caller" speeking

    @critical
    Scenario: caller may give a call to a recipient and recipient may decline it
        When "caller" calls to "recipient"
        Then "recipient" should see "caller" ringing

        When "recipient" declines call
        Then "caller" should not hear "recipient" speaking
        # and probably sees something
        And "recipient" should not hear "caller" speeking
    # and probably sees something

    @critical
    Scenario: caller can drop the call
        Given "caller" has a call with "recipient"
        When "caller" drops the call
        Then "recipient" should not hear "caller" speaking
        # and probably sees something
        And "recipient" should not hear "caller" speaking
    # and probably sees something

    @major
    Scenario: The call should be terminated when recipient drops the call
        Given "caller" has a call with "recipient"
        When "recipient" drops the call
        Then "caller" should not hear "recipient" speaking
        # and probably sees something
        And "recipient" should not hear "caller" speaking
    # and probably sees something

    @major
    Scenario: caller hears long signal while waiting
        When "caller" calls to "recipient"
        Then "caller" hears long signal while waiting for call to be accepted

    @moderate
    Scenario: caller should see timer showing call duration properly
        Given "caller" has a call with "recipient"
        Then "caller" should see timer showing call duration properly

    @major
    Scenario Outline: caller can not call to invalid number
        When "caller" types "<number>" to the number field
        Then "caller" should hear error message "calling to invalid number"

        Examples:
            | number               |
            | 12                   |
            | 12345678901234567890 |
            | +1111111111          |

    @major
    Scenario Outline: caller can not call to short or special numbers
        When "caller" types "<number>" to the number field
        Then "caller" should hear error message "caling to short or special numbers is not allowed"

        Examples:
            | number |
            | 911    |
            | *111#  |

    @moderate
    Scenario: caller may call to contact
        When "caller" calls to "recipient" by contact name
        Then "recipient" should see "caller" ringing
        And "caller" should see "recipient" phone number and name


    @moderate
    Scenario: caller may call to teammate
        When "caller" calls to "recipient" by teammate name
        Then "recipient" should see "caller" ringing
        And "caller" should see "recipient" phone number and name

    @moderate
    Scenario: caller sees error message if service is down
        Given "caller" has a call with "recipient"
        When service is down
        Then "caller" should see error message "Something went wrong, try again later"
        And "caller" should see link "Contact support"

    @low
    Scenario: caller can't call himself
        When "caller" calls to "caller"
        Then "caller" should see error message "You can not call yourself"
    # It's funny, but it right now it's possible to call yourself

    @low
    Scenario: caller's number phone code should be selected by default
        When "caller" cleans the number field
        Then "caller" should see his phone code selected by default

    @low
    Scenario: caller should see phone code of the country parsed correctly
        When "caller" types "+1" to the number field
        Then "caller" should see phone code of "United States" parsed correctly

        When "caller" clears the number field
        And "caller" types "+34" to the number field
        Then "caller" should see phone code of "Spain" parsed correctly

        Examples:
            | number               |
            | 12                   |
            | 12345678901234567890 |
            | +1111111111          |
