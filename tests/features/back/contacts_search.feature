Feature: Contacts search
    As an API user
    A want to be able to search for contacts
    So that I can find contacts by phone number, email, name, etc.

    Scenario: Search for contacts by phone number
        Given authorized user searches for contacts by phone_number "+33652556756"
        Then response code should be 200
        And "/contacts/search" response should be valid
        And response should contain 1 contact
        And contact "test_contact" should be found

    Scenario: Search by non-existing phone
        Given authorized user searches for contacts by phone_number "+1231231231231231231231231232"
        Then response code should be 200
        And "/contacts/search" response should be valid
        And response should contain 0 contacts

    Scenario: Search for contacts by part of the phone number
        Given authorized user searches for contacts by phone_number "+3"
        Then response code should be 200
        And found contacts should have phone_numbers with at least one value starting with "+3"

    Scenario: Search for contact by email
        Given authorized user searches for contacts by email "test@acme.com"
        Then response code should be 200
        And "/contacts/search" response should be valid
        And response should contain 1 contacts

    Scenario: Unauthorized search for contacts
        Given unauthorized user searches for contacts by phone_number "+33652556756"
        Then response code should be 401
        And response message should be "Unauthorized"

    Scenario: Search for contact created after date
        Given authorized user searches for contacts by from "1672995969"
        Then response code should be 200
        And found contacts should have created_at more than "1672995969"

    Scenario: Search for contact created before date
        Given authorized user searches for contacts by to "1672995969"
        Then response code should be 200
        And found contacts should have created_at less than "1672995969"

    Scenario: Default ordering is ascending by created_at
        Given authorized user searches for contacts
        Then response code should be 200
        And found contacts should be ordered by created_at asc

    Scenario: Order by updated_at desc
        Given authorized user searches for contacts ordered by updated_at desc
        Then response code should be 200
        And found contacts should be ordered by updated_at desc

    Scenario: Search allows pagination
        Given authorized user searches for contacts
        Then response code should be 200
        And response meta should have next page link


