# QA Test for Aircall 

This repo has a solution for the QA tests provided by Aircall.

* test-back.md
* test-front.md
* test-manual.md

As far as context is `You work at Aircall….`, I decided to use the same approach for all tests. 

So, test cases are described in Gherkin language, so that they can be used as a single source of truth for all parties involved in the project.

Also, I put API and UI tests in the same repo, as they are related to the same project, and API steps may be reused in UI tests as pre- and post conditions.

# Test cases

Test cases for all tests are described in Gherkin language and can be found in the folders representing the test task files: 
- features/back has features for test-back.md
- features/front has features for test-front.md
- features/manual has features for test-manual.md

