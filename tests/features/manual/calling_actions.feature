Feature: Outbound Call Actions
    As an caller,
    I want to be able to perform actions during the call

    Background:
        Given "caller" is logged in to the phone
        And "caller" has a call with "recipient"

    @critical
    Scenario: caller should see call actions and info during the call
        Then "caller" should see call actions
        And "caller" should see network status
        And "caller" should see call "recipient" info
        And "caller" should see his number

    @major
    Scenario: caller can mute
        When "caller" clicks on mute button
        Then "caller" should see that call is muted
        And "recipient" should not hear "caller"

    @major
    Scenario: caller can unmute
        When "caller" clicks on mute button
        Then "caller" should see that call is muted
        
        When "caller" clicks on unmute button
        Then "caller" should see that call is unmuted
        And "recipient" should hear "caller"

    @major
    Scenario: caller can hold the call
        When "caller" clicks on hold button
        Then "caller" should see that call is on hold
        And "recipient" should not hear "caller"
        And "recipient" should hear hold music

    @major
    Scenario: caller can unhold the call
        When "caller" clicks on hold button
        Then "caller" should see that call is on hold

        When "caller" clicks on unhold button
        Then "caller" should see that call is unholded
        And "recipient" should hear "caller"
        And "recipient" should not hear hold music
    
    @major
    Scenario: caller can transfer the call
    # Not sure, how this functionality should work, because I have only one caller
        When "caller" transfers the call to "caller2"
        Then "caller" should see that call is transferred
        And "caller" should not hear "recipient"

        And "caller2" should see that call is transferred
        And "caller2" should hear "recipient"
        
        And "recipient" should hear "caller2"
        And "recipient" should not hear "caller"
        
    @major
    Scenario: caller can add to call another caller
    # Not sure, how this functionality should work, because I have only one caller
        When "caller" adds "caller2" to the call
        Then "caller" should see that "caller2" is added to the call

        And "caller2" should see that he is added to the call
        And "caller2" should hear "recipient"

        And "recipient" should hear "caller2"
        And "recipient" should hear "caller"

    @major
    Scenario: caller can call separately 
        When "caller" calls to "caller2" separately
        Then "caller" should hear "caller2"
        And "caller" shoould not hear "recipient"

        And "caller2" should hear "caller"
        And "caller2" should not hear "recipient"

        And "recipient" should hear waiting music

    @major
    Scenario: caller can use keypad
        # This case should probably require specific setup
        Given "recipient" has an action on button 1
        When "caller" clicks on keypad button 1
        Then "caller" should hear the assigned action sound

    @major
    Scenario: caller can record the call
        When "caller" clicks on record button
        Then "caller" should see that call is recording

        When "caller" drops the call
        And "caller" opens the call info
        Then "caller" should see call recording
        And "caller" can hear the call recording

    @major
    Scenario: caller can pause the recording
        When "caller" clicks on record button
        Then "caller" should see that call is recording

        When "caller" pause recording
        Then "caller" should see that recording is not running

        When "caller" drops the call
        And "caller" opens the call info
        Then "caller" should see call recording
        And "caller" can hear the call recording

    @major
    Scenario: caller can resume the recording
        When "caller" clicks on record button
        Then "caller" should see that call is recording

        When "caller" pause recording
        Then "caller" should see that recording is not running

        When "caller" resume recording
        Then "caller" should see that recording is running

        When "caller" drops the call
        And "caller" opens the call info
        Then "caller" should see call recording
        And "caller" can hear the call recording with pause

    @minor
    Scenario: caller can copy phone number
        When "caller" clicks on phone number
        Then "caller" should see that phone number is copied to clipboard

    @moderate
    Scenario: caller can hide a call
        When "caller" clicks on hide button
        Then "caller" should see lowerbar with hidden call
        And "caller" should be on "keypad" page

    @moderate
    Scenario: caller can expand a call 
        When "caller" clicks on hide button
        Then "caller" should see lowerbar with hidden call

        When "caller" clicks on "Expand" button
        Then "caller" should see call expanded
        And "caller" should be on "incall" page

    @moderate
    Scenario: caller can add number to contact    
        Given "recipient" number is not saved in contacts
        When "caller" clicks on "Add contact" button
        Then "caller" should see "New contact" modal

        When "caller" fills in "First name" with "recipient" name 
        And "caller" clicks "Save"
        Then "caller" should see "recipient" name in contacts

        When "caller" clicks on hide button
        And "caller" navigates to "people" page 
        Then "caller" should see "recipient" name in contacts
