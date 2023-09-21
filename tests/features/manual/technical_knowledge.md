# QA technical test - Manual

## Technical knowledge for QA

### What is a specification? 
It's not clear what kind of specification is meant here. I recall the following types of specifications:
- **Software requirements specification** - the document, that describes the requirements for the software to be developed. It lays out functional and non-functional requirements. It may also contain use cases, user stories, etc.
- **Test specification** - the document, that describes the test cases for the software, what is to be tested, how it is to be tested, what are the expected results, etc.

### What is a test plan? 
As per ISTQB definition: "**Test Plan** is A document describing the scope, approach, resources, and schedule of intended test activities." It includes information about test items, features to be tested and features not to be tested, testing tasks, test environment, responsibilities, risks, etc. The test plan structure is specified in [IEEE 829 standard](https://en.wikipedia.org/wiki/Software_test_documentation) .

The test plan and test specification are different documents. The test plan is a high-level document, that describes the overall testing approach, while the test specification is a low-level document, that describes the test cases. The test specification is based on the test plan, and the test plan is based on the software requirements specification.

### What is a test case? 
**Test case** is a set of test inputs, execution conditions, and expected results for verifying a specific feature or function of software. 
Usually, a test case has the following structure:
- Test case ID
- Test case description or summary
- Test steps
- Expected results
- Prerequisites
Additionally, a test case may contain:
- Description
- Author
- Extra-fields (automation, feature, app versions, etc.)
A written test case should also contain a place for the actual result.

### What is a bug? What is the purpose of a bug report? What are the parts of a bug report? 
**Bug** is a defect in the software, that causes it to behave in an unexpected way. The purpose of a bug report is to provide information about the bug to the development team, so that they can fix it. The bug report should contain the following parts:
- Summary
- Description
- Steps to reproduce
- Expected result
- Actual result
- Severity
- Priority
- Environment (browser, OS, app version, etc.)
- Attachments (screenshots, logs, etc.)
Usually, priority and severity are defined by the development team and/or business (PMs, POs, BAs, etc.), but the tester may also provide their opinion on these fields.

### What is unit, functional, integration, regression, black/white box, acceptance testing?
The question has a mixture of different types and levels of testing, so let's keep it in order. 

![testing types](https://browserstack.wpenginepowered.com/wp-content/uploads/2023/03/Types-of-software-testing-1.png)

First of all, there are two types of testing: **functional** and **non-functional** (similar to the functional and non-functional requirements). Functional testing is testing the functionality of the software, while non-functional testing is testing the non-functional aspects of the software, such as performance, security, usability, etc.

Functional testing can be performed on different levels of the software, and the most common levels are:
- **Unit** - testing the smallest testable parts of the software, usually functions or methods. 
- **Integration** - testing the integration of different parts of the software. 
- **System** - testing the whole system as a whole. 
- **Acceptance** - testing the software from the user's perspective

For performing testing we may use different approaches, such as:
- **Black-box testing** - testing the software without knowing its internal structure.
- **White-box testing** - testing the software with knowing its internal structure.

**Regression testing** is the process of reusing functional and non-functional tests after changes to ensure that the changes did not break the existing functionality.


### How does browsing the web work? Or, how many requests does it take to load a web page?

This question might have a variety of answers depending on the expected level of detail. I will try to provide a high-level overview of the process.

When a user enters a URL in the browser, the browser sends a request to the server. The server response (usually, the HTML page) is rendered by the browser. The HTML page may contain links to other resources, such as CSS, JS, images, etc. The browser sends requests for these resources to the server (this or another). The browser renders the resources and displays the page to the user. The JS code may request extra resources as well using AJAX requests.

So, the number of requests may vary from 1 to infinity.
