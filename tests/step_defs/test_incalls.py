import pytest
import threading

from pytest_bdd import scenarios, given, when, then, parsers
from tests.data.account_provider import AccountProvider
from tests.pages.phone.incall import InCallPage
from tests.pages.phone.keyboard import KeyboardPage
from tests.pages.phone.ringing import RingingPage

from tests.pages.phone.login import LoginPage
from tests.pages.phone.ringing_incoming import RingingIncomingPage
from tests.utils.session_manager import SessionManager
from tests.utils.session_provider import SessionProvider


scenarios("../features/front/standard_incall_actions.feature")


@pytest.fixture
def sessionManager():
    """
    Fixture to manage sessions
    As far as the precondition is very long-running, I decided to perform the tests in the same call
    This might cause the cascading failures, so need to check on practice
    """
    try:
        sessions = SessionManager()
        init_sessions_in_parallel(["caller", "recipient"], sessions)

        user_gives_call("caller", "recipient", sessions)
        user_accepts_call("recipient", "caller", sessions)

        user_should_be_on_call("caller", sessions)
        user_should_be_on_call("recipient", sessions)

        yield sessions
    finally:
        sessions.quit()


@given(parsers.parse("{user} is logged in to the phone"))
def user_is_logged_in(user: str, sessionManager: SessionManager):
    """
    Initialize a session for a user (start browser, login)
    This method should probable be a fixture as well, but I'm nor sure how to handle it properly

    Parameters
    ----------
    session_name : str
        Name of the session
    account : Account
        Account to login with
    sessions : SessionManager
        Session manager to store the session

    Returns
    -------
    None

    """
    session = SessionProvider.init_chrome_session()
    sessionManager.add(user, session)
    account = AccountProvider.get_instance().get_account(user)
    keyboard_page = LoginPage(session).open().api_login(account, skip_wizard=True)
    keyboard_page.wait_for_page_to_load()


@when(parsers.parse('{caller} calls to "{recipient}" by number'))
def user_gives_call(
    caller: str, recipient: str, sessionManager: SessionManager
) -> RingingPage:
    """
    Call to a recipient by number

    Parameters
    ----------
    caller : str
        Name of the caller
    recipient : str
        Name of the recipient

    Returns
    -------
    RingingPage

    """
    caller_session = sessionManager.get(caller)
    recipient_account = AccountProvider.get_instance().get_account(recipient)

    ringing_page = (
        KeyboardPage(caller_session)
        .wait_for_page_to_load()
        .call_to(recipient_account.phone)
    )
    return ringing_page.wait_for_page_to_load().should_have_contact_name(
        recipient_account.phone
    )


@when(parsers.parse("{recipient} accepts the call from {caller} by number"))
def user_accepts_call(
    recipient: str, caller: str, sessionManager: SessionManager
) -> RingingPage:
    """
    Accepts the call from caller

    Parameters
    ----------
    recipient : str
        Name of the recipient
    caller : str
        Name of the caller

    Returns
    -------
    InCallPage
    """
    caller_account = AccountProvider.get_instance().get_account(caller)

    ringing_page = RingingIncomingPage(sessionManager.get(recipient))
    return ringing_page.wait_for_page_to_load().should_have_contact_name(
        caller_account.phone
    ).pickup_call()


@then(parsers.parse("{user} should be on call"))
def user_should_be_on_call(user: str, sessionManager: SessionManager) -> InCallPage:
    """
    Assert that the user is on call

    Parameters
    ----------
    user : str
        Name of the user

    Returns
    -------
    InCallPage
    """
    session = sessionManager.get(user)
    in_call_page = InCallPage(session)
    return in_call_page.wait_for_page_to_load()


def init_sessions_in_parallel(names: list, sessionManager: SessionManager) -> None:
    """
    Initialize sessions in parallel

    Parameters
    ----------

    names : list
        List of session names
    sessions : SessionManager
        Session manager to store the sessions

    Returns
    -------
    None
    """

    threads = []
    AccountProvider.get_instance()  # Load accounts
    for session_name in names:
        thread = threading.Thread(
            target=user_is_logged_in, args=(session_name, sessionManager)
        )
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
