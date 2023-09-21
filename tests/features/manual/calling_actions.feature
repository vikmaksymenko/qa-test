Feature: Outbound Call Actions
    As an agent,
    I want to be able to perform actions during the call

    Background:
        Given: "agent" has a call with "client"

    @critical
    Scenario: Agent should see call actions and info during the call
        Then "agent" should see call actions
        And "agent" should see network status
        And "agent" should see call "client" info
        And "agent" should see his number

    @major
    Scenario: Agent can mute
        When "agent" clicks on mute button
        Then "agent" should see that call is muted
        And "client" should not hear "agent"

    @major
    Scenario: Agent can unmute
        When "agent" clicks on mute button
        Then "agent" should see that call is muted
        
        When "agent" clicks on unmute button
        Then "agent" should see that call is unmuted
        And "client" should hear "agent"

    @major
    Scenario: Agent can hold the call
        When "agent" clicks on hold button
        Then "agent" should see that call is on hold
        And "client" should not hear "agent"
        And "client" should hear hold music

    @major
    Scenario: Agent can unhold the call
        When "agent" clicks on hold button
        Then "agent" should see that call is on hold

        When "agent" clicks on unhold button
        Then "agent" should see that call is unholded
        And "client" should hear "agent"
        And "client" should not hear hold music
    
    @major
    Scenario: Agent can transfer the call
    # Not sure, how this functionality should work, because I have only one agent
        When "agent" transfers the call to "agent2"
        Then "agent" should see that call is transferred
        And "agent" should not hear "client"

        And "agent2" should see that call is transferred
        And "agent2" should hear "client"
        
        And "client" should hear "agent2"
        And "client" should not hear "agent"
        
    @major
    Scenario: Agent can add to call another agent
    # Not sure, how this functionality should work, because I have only one agent
        When "agent" adds "agent2" to the call
        Then "agent" should see that "agent2" is added to the call

        And "agent2" should see that he is added to the call
        And "agent2" should hear "client"

        And "client" should hear "agent2"
        And "client" should hear "agent"

    @major
    Scenario: Agent can call separately 
        When "agent" calls to "agent2" separately
        Then "agent" should hear "agent2"
        And "agent" shoould not hear "client"

        And "agent2" should hear "agent"
        And "agent2" should not hear "client"

        And "client" should hear waiting music

    @major
    Scenario: Agent can use keypad
        # This case should probably require specific setup
        Given "client" has an action on button 1
        When "agent" clicks on keypad button 1
        Then "agent" should hear the assigned action sound

    @major
    Scenario: Agent can record the call
        When "agent" clicks on record button
        Then "agent" should see that call is recording

        When "agent" drops the call
        And "agent" opens the call info
        Then "agent" should see call recording
        And "agent" can hear the call recording

    @major
    Scenario: Agent can pause the recording
        When "agent" clicks on record button
        Then "agent" should see that call is recording

        When "agent" pause recording
        Then "agent" should see that recording is not running

        When "agent" drops the call
        And "agent" opens the call info
        Then "agent" should see call recording
        And "agent" can hear the call recording

    @major
    Scenario: Agent can resume the recording
        When "agent" clicks on record button
        Then "agent" should see that call is recording

        When "agent" pause recording
        Then "agent" should see that recording is not running

        When "agent" resume recording
        Then "agent" should see that recording is running

        When "agent" drops the call
        And "agent" opens the call info
        Then "agent" should see call recording
        And "agent" can hear the call recording with pause

    @minor
    Scenario: Agent can copy phone number
        When "agent" clicks on phone number
        Then "agent" should see that phone number is copied to clipboard

    @moderate
    Scenario: Agent can hide a call
        When "agent" clicks on hide button
        Then "agent" should see lowerbar with hidden call
        And "agent" should be on "keypad" page

    @moderate
    Scenario: Agent can expand a call 
        When "agent" clicks on hide button
        Then "agent" should see lowerbar with hidden call

        When "agent" clicks on "Expand" button
        Then "agent" should see call expanded
        And "agent" should be on "incall" page

    @moderate
    Scenario: Agent can add number to contact    
        Given "client" number is not saved in contacts
        When "agent" clicks on "Add contact" button
        Then "agent" should see "New contact" modal

        When "agent" fills in "First name" with "client" name 
        And "agent" clicks "Save"
        Then "agent" should see "client" name in contacts

        When "agent" clicks on hide button
        And "agent" navigates to "people" page 
        Then "agent" should see "client" name in contacts
