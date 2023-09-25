import requests
import os
import json
import jsonschema

from pytest_bdd import scenarios, parsers, given, then

from tests.utils.api import ApiUtils
from tests.utils.utils import load_json

scenarios("../features/back/contacts_search.feature")

API_URL = os.getenv("API_BASE_URL")
AUTHORIZATION_TOKEN = ApiUtils.prepare_token()


@given(
    parsers.parse("{user_name} user searches for contacts"),
    target_fixture="search_contact_response",
)
def search_contact_response(user_name: str) -> requests.Response:
    """
    Search for contacts with default parameters

    Parameters
    ----------
    user_name : str
        Name of the user to search for contacts. If the user is "authorized", the request will be sent with the Authorization header
    Returns
    -------
    requests.Response
    """
    return search_for_contacts(user_name)


@given(
    parsers.parse('{user_name} user searches for contacts by {field} "{value}"'),
    target_fixture="search_contact_response",
)
def search_contact_response(
    user_name: str, field: str, value: str
) -> requests.Response:
    """
    Search for contacts by specified field and value


    Parameters
    ----------
    user_name : str
        Name of the user to search for contacts. If the user is "authorized", the request will be sent with the Authorization header
    field : str
        Field to search by
    value : str
        Value of the field to search by
    """
    return search_for_contacts(user_name, {field: value})


@given(
    parsers.parse(
        "{user_name} user searches for contacts ordered by {order_by} {direction}"
    ),
    target_fixture="search_contact_response",
)
def search_contact_response(
    user_name: str, order_by: str, direction: str
) -> requests.Response:
    """
    Search for contacts and order the results


    Parameters
    ----------
    user_name : str
        Name of the user to search for contacts. If the user is "authorized", the request will be sent with the Authorization header
    order_by : str
        Field to order by
    direction : str
        Direction of the order (asc or desc)
    """
    params = {"order_by": order_by}
    if direction is not None:
        params["order"] = direction

    return search_for_contacts(user_name, params)


@then(parsers.parse("response code should be {status_code:d}"))
def response_code_should_be(
    search_contact_response: requests.Response, status_code: int
):
    """Check that the response code is as expected"""
    assert search_contact_response.status_code == status_code


@then(parsers.parse('"{endpoint}" response should be valid'))
def validate_response(endpoint: str, search_contact_response: requests.Response):
    """Validate the response against the schema"""
    schema_file = endpoint.replace("/", "_") + ".json"
    schema_path = f"tests/resources/api/schemas/{schema_file}"

    with open(schema_path) as json_file:
        schema = json.load(json_file)
        jsonschema.validate(search_contact_response.json(), schema)


@then(parsers.parse("response should contain {count:d} contact"))
@then(parsers.parse("response should contain {count:d} contacts"))
def contacts_search_should_have_count_of_contacts(
    count: int, search_contact_response: requests.Response
):
    """Check that the response contains the expected number of contacts"""
    assert len(search_contact_response.json()["contacts"]) == count


@then(parsers.parse('response message should be "{message}"'))
def response_message_should_be(
    message: str, search_contact_response: requests.Response
):
    """Check that the response message is as expected"""
    assert search_contact_response.json()["message"] == message


@then(parsers.parse('contact "{contact_name}" should be found'))
def contact_should_be_found(
    contact_name: str, search_contact_response: requests.Response
):
    """Check that the response contains the expected contact"""
    expected = load_json(f"tests/resources/api/data/{contact_name}.json")
    contacts = search_contact_response.json()["contacts"]
    contact = next((c for c in contacts if c["id"] == expected["id"]), None)
    assert contact is not None


@then(
    parsers.parse(
        'found contacts should have {field} with at least one value starting with "{value}"'
    )
)
def found_contacts_should_have_at_least_one_value_starting_with_substr(
    field: str, value: str, search_contact_response: requests.Response
):
    """
    Check that the response has collection of fields,
    and there's at least one field value starting with the specified substring
    """

    contacts = search_contact_response.json()["contacts"]

    contacts_without_valid_number = []
    for contact in contacts:
        field_values = contact[field]
        number_found = False
        for field_value in field_values:
            if field_value["value"].startswith(value):
                number_found = True
                break
        if not number_found:
            contacts_without_valid_number.append(contact)
    assert len(contacts_without_valid_number) == 0


@then(parsers.parse('found contacts should have {field} {action} than "{value:d}"'))
def found_contacts_should_have_value_more_or_less_then_specified(
    field: str, action: str, value: int, search_contact_response: requests.Response
):
    """
    Check that the response field has value more or less than specified

    Parameters
    ----------
    field : str
        Field to check
    action : str
        Action to perform (more or less)
    value : int
        Value to compare with
    """
    contacts = search_contact_response.json()["contacts"]

    for contact in contacts:
        if action == "less":
            assert contact[field] < value
        elif action == "more":
            assert contact[field] > value
        else:
            raise ValueError(f"Unknown action {action}")


@then(parsers.parse("found contacts should be ordered by {field} {directions}"))
def found_contacts_should_be_ordered(
    field: str, directions: str, search_contact_response: requests.Response
):
    """
    Check that the response contacts are ordered by the specified field in specified direction

    Parameters
    ----------
    field : str
        Field to order by
    directions : str
        Direction of the order (asc or desc)
    """
    contacts = search_contact_response.json()["contacts"]

    for i in range(len(contacts) - 1):
        if directions == "asc":
            assert contacts[i][field] <= contacts[i + 1][field]
        elif directions == "desc":
            assert contacts[i][field] >= contacts[i + 1][field]
        else:
            raise ValueError(f"Unknown sort direction {directions}")


@then("response meta should have next page link")
def found_contacts_should_be_ordered(search_contact_response: requests.Response):
    """Check that the response meta has next page link"""
    meta = search_contact_response.json()["meta"]
    current_page = meta["current_page"]
    per_page = meta["per_page"]
    assert meta["next_page_link"] is not None and meta["next_page_link"].endswith(
        f"&page={current_page + 1}&per_page={per_page}"
    )


def search_for_contacts(user_name: str, params: dict = {}) -> requests.Response:
    """
    Search for contacts with specified parameters

    Parameters
    ----------
    user_name : str
        Name of the user to search for contacts. If the user is "authorized", the request will be sent with the Authorization header
    params : dict
        Parameters to search by

    Returns
    -------
    requests.Response
    """

    headers = {"Content-Type": "application/json"}
    if user_name == "authorized":
        headers["Authorization"] = AUTHORIZATION_TOKEN

    endpoint = "/contacts/search"

    return requests.get(API_URL + endpoint, params=params, headers=headers)
