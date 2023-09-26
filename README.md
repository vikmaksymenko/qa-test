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

# Automation

## Requirements
* Python 3.11
* Docker 

## Front-end automation 

I was thinking about using Playwright for automated testing, because it allows to automate both UI and API test. However, after careful consideration, I decided to use Selenium for front-end automation. Here are the reaisons for that. 
1. From my perspective, the most important validation for the phone is to check that caller and recipient can hear each other. In order to achieve this, we need to record audio on hosts, and I'm not sure that it is possible withing the same host. So I would suggest using Docker containers for caller and recipient sessions. Selenium grid can be run in auto-scalable group. Alternatively, [Selenoid](https://aerokube.com/selenoid/latest/) can be used for the same purpose. However, browser images should be extended with extra tools like pulseaudio, ffmpeg, etc. I'm not aware of other tools besides Selenium that allow creation of sessions on different hosts (maybe Playwright can, but investigation is required).
This audion check is not implemented in the test task solution, because it's realization is time consuming and requires extra resources. Also, it's not specified in test plan. If the tests in test plans are focusing to check front-end functionality isolated with mocked back-end, then the audio checks are redundant.
2. There are web, mobile and desktop versions of the phone. Selenium and Appium can be used for all of them. Playwright has experimental support of Android and Electron apps, but it is not production-ready yet.

### Testing infrastructure

In order to run tests on separate containers, I recommend using [Dynamic Selenium grid](https://github.com/SeleniumHQ/docker-selenium#dynamic-grid). It will create separate containers for each test session and terminate them after the session is finished.


#### MacOS and Linux
```bash
docker pull selenium/standalone-chrome:latest
docker run --rm --name selenium-docker -p 4444:4444 \
    -v ${PWD}/infra/config.toml:/opt/bin/config.toml \
    -v ${PWD}/infra/assets:/opt/selenium/assets \
    -v /var/run/docker.sock:/var/run/docker.sock \
    selenium/standalone-docker:latest
```

#### Windows
```bash
docker pull selenium/standalone-chrome:latest
docker run --rm -d --name selenium-docker -p 4444:4444 `
    -v ${PWD}/infra/config.toml:/opt/bin/config.toml `
    -v ${PWD}/infra/assets:/opt/selenium/assets `
    -v /var/run/docker.sock:/var/run/docker.sock `
    selenium/standalone-docker:latest
```

### Preparing test data 

In order to run tests, you need to create a test account and create a JSON file `accounts.json` with the test data in the following format:

```json
{
    "<USER_NAME>": {
        "email": "<EMAIL>",
        "password": "<PASSWORD>",
        "phone": "<PHONE>",
        "id": <USER_ID:int>,
        "company_id": <COMPANY_ID:int>
    },
    "<OTHER_USER>": {
        ...
    }
}
```
Notice that the user name must match to the one, specified in the feature files.
The path to the file should be specified in the env variable `PHONE_ACCOUNTS_FILE` or in the `.env` file in the root of the project.

Additionaly, you may update the base URL to the phone app by setting `PHONE_BASE_URL` env variable. Default value is `https://phone.aircall.io/`.

### Running tests

#### Install dependencies
```bash
pip install -r requirements.txt
```

#### Run tests (Windows)

```bash
python -m pytest .\tests\step_defs\test_incalls.py
```

#### Run tests (MacOS and Linux)


```bash
python -m pytest tests/step_defs/test_incalls.py
```


### Running tests in parallel 

Test parallelization is not implemented due to the lack ot testing accounts. 


## API Tests

### Prerequisites

Set the following environment variables or add them to the `.env` file in the root of the project:
* `API_BASE_URL` - base URL for the API. Default value is `https://api.aircall.io/`.
* `API_ID` - API ID
* `API_TOKEN` - API token

### Running tests

Install dependencies similarly to the front-end tests and run the following command:

#### Run tests (Windows)

```bash
python -m pytest .\tests\step_defs\test_api.py
```

#### Run tests (MaoOS and Linux)


```bash
python -m pytest tests/step_defs/test_api.py
```

### Test parallelization

Test parallelization is not implemented due to the API requests rate limit.

## Reporting 

I decided to use [Allure Framework](https://docs.qameta.io/allure/) for generating HTML report. In order to use, add parameter `--alluredir=allure-results` to the pytest command. 

```bash
python -m pytest  --alluredir=allure-results
```

In order to generate or open report, install [allure command line tool](https://docs.qameta.io/allure/#_installing_a_commandline). Then, run the following command to generate HTML report:

```bash
allure generate allure-results
```

This will generate an HTML report in the `allure-report` folder. 

For generating and opening report, run the following command:

```bash
allure serve allure-results
```

It will generate report in the temp folder, start webserver and open the report in the browser.