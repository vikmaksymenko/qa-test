Feature: Standard incall - Actions
    As an recipient
    I want to perform actions during the call

    Scenario: Sample scenario
        Then caller should be on call
        And recipient should be on call

        # Then recipient should see incall page

    # Background:
    #     Given "caller" is logged in to the phone
    #     And "recipient" is logged in to the phone
    #     And "caller" has a call with "recipient"

    # Scenario: recipient can mute
    #     When "recipient" clicks on "mute" button
    #     Then "recipient" should see "mute" button toggles in red # Does it really turns red? Is it a bug or outdated test case? 
    
    # Scenario: recipient can hold the call
    #     When "recipient" clicks on "hold" button
    #     Then "recipient" should see "mute" button toggles in red # Does it really turns red? Is it a bug or outdated test case? 

    # Scenario: recipient can use keyboard
    #     When "recipient" clicks on "keyboard" button
    #     Then "recipient" should see "keyboard" modal opened

    #     When "recipient" input "+123" on keyboard using buttons
    #     Then "recipient" should see "+123" inputed


    # Scenario: recipient can not input more then 23 digits
    #     When "recipient" clicks on "keyboard" button
    #     Then "recipient" should see "keyboard" modal opened

    #     When "recipient" input "+12345678901234567890123456789" on keyboard
    #     Then "recipient" should see "+12345678901234567890123" inputed
        
    # Scenario: recipient can reopen keyboard
    #     When "recipient" clicks on "keyboard" button
    #     Then "recipient" should see "keyboard" modal opened

    #     When "recipient" closes keyboard
    #     Then "recipient" should see phone page 

    #     When "recipient" clicks on "keyboard" button
    #     Then "recipient" should see "keyboard" modal opened
    #     And "recipient" should see empty keyboard input
        

    # Scenario: recipient can assign call
    #     When "recipient" clicks on "assign" button
    #     Then "recipient" should see "assign" modal opened

    #     When "recipient" selects "agent" from "assign" modal
    #     Then "recipient" should see success message

    #     # ???
    #     # "When clicking on an agent, view changes"	modal and icon in the submenu
        
    # Scenario: recipient can tag call
    #     When "recipient" clicks on "tag" button
    #     Then "recipient" should see "tag" modal opened

    #     When "recipient" adds tag to call
    #     And "recipient" terminates the call
    #     And "recipient" opens feed
    #     Then "recipient" should see tag on the last call

    # Scenario: recipient can add comment
#     "- Block should expand on click/hover
# - Comment should be temporary saved
# - On call ended, keyboard button should change for a ""✓"" button
# - On click, comment is saved and go back to keyboard occurs"

    # Scenario: recipient can transfer call
    # Modal appears on button press

    # Scenario: recipient can have concurrent call
    # Modal appears on button press

    # Scenario: recipient can create contact
    # If an external number isn't bound to a contact, should be able on the "+" button to go to the new contact page and add it. On save, it should go back to incall view and update the view

    # The scenario below is not clear enough, the clarification required
    # Scenario: wrap up time 
#     "1. Go to Keypad page
# 2. Enter number
# 3. Dial the number
# 4. Disconnect the call
# Validate - user is unavailable"

