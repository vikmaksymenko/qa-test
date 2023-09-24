Feature: Standard incall - Actions
    As an recipient
    I want to perform actions during the call

    Background:
        Given caller should be on call
        And recipient should be on call

    Scenario: recipient can mute
        When recipient clicks on "Mute" action button
        # Does it really turns red? Is it a bug or outdated test case? 
        Then recipient should see "Mute" action button toggles in red 

    Scenario: recipient can hold the call
        When recipient clicks on "Hold" action button
        # Does it really turns red? Is it a bug or outdated test case? 
        Then recipient should see "Hold" action button toggles in red 

    # THE OTHER CASES WERE NOT IMPLEMENTED, BECAUSE MY TRIAL EXPIRED

    # Scenario: recipient can use keyboard
    #     When recipient clicks on "keyboard" button
    #     Then recipient should see "keyboard" modal opened

    #     When recipient input "+123" on keyboard using buttons
    #     Then recipient should see "+123" inputed


    # Scenario: recipient can not input more then 23 digits
    #     When recipient clicks on "keyboard" button
    #     Then recipient should see "keyboard" modal opened

    #     When recipient input "+12345678901234567890123456789" on keyboard
    #     Then recipient should see "+12345678901234567890123" inputed
        
    # Scenario: recipient can reopen keyboard
    #     When recipient clicks on "keyboard" button
    #     Then recipient should see "keyboard" modal opened

    #     When recipient closes keyboard
    #     Then recipient should see phone page 

    #     When recipient clicks on "keyboard" button
    #     Then recipient should see "keyboard" modal opened
    #     And recipient should see empty keyboard input
        

    # Scenario: recipient can assign call
    #     When recipient clicks on "assign" button
    #     Then recipient should see "assign" modal opened

    #     When recipient selects "agent" from "assign" modal
    #     Then recipient should see success message

    #     # ???
    #     # "When clicking on an agent, view changes"	modal and icon in the submenu
        
    # Scenario: recipient can tag call
    #     When recipient clicks on "tag" button
    #     Then recipient should see "tag" modal opened

    #     When recipient adds tag to call
    #     And recipient terminates the call
    #     And recipient opens feed
    #     Then recipient should see tag on the last call
