**AIRCALL-1** - Agent may give a call to himself
================================================

Description
-----------

User can type his line number and call himself.

Steps to reproduce
------------------

1. Login to the phone application
2. Go to the keypad page
3. Type the line number in the input field
4. Click the call button

Expected result
---------------

User should see warning message that he is calling himself, call button should be disabled.

Actual result
-------------

User can call himself and hear long beeps. If the user drops the call he may hear the inbound call sound.

Severity
--------
Minor

Priority
--------
Low

Environment 
-----------
Windows desktop app version 2.36.3
