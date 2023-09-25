from tests.data.account import Account
from tests.pages.phone.incall import InCallPage
from tests.pages.phone.keyboard import KeyboardPage
from tests.pages.phone.onboarding import OnboardingPage
from tests.pages.phone.phone_base import BasePhonePage
from tests.utils.int_api.id_api import IdApi
from tests.utils.utils import current_time_milis

from selenium import webdriver


class LoginPage(BasePhonePage):
    """
    Login page of the phone app
    """

    def __init__(self, driver: webdriver.Remote) -> None:
        BasePhonePage.__init__(self, driver)
        self._endpoint = "/login"

    def api_login(self, account: Account, skip_wizard: True) -> BasePhonePage:
        """
        Login to the phone app using the internal API.
        The API response is stored in the local storage of the browser.
        It allows to bypass the login page.
        Additionally, the user id is stored in the local storage of the browser.

        Parameters
        ----------
        account : Account
            Account to login with
        skipWizard : bool
            Whether to skip the wizard or not

        Returns
        -------
        OnboardingPage or InCallPage depending on the skipWizard parameter
        """
        current_time = current_time_milis()
        login_response = IdApi.login(account.email, account.password)

        login_data = {"data": login_response, "lastUpdated": current_time}
        self._set_local_storage_item("aircall-cache-last-logged-in", login_data)

        last_user_id = {"data": account.id, "lastUpdated": current_time}
        self._set_local_storage_item("aircall-cache-last-user-id", last_user_id)

        user_data = {
            "data": {
                "state": {
                    "auth": {"strategy": "password"},
                    "user": {"id": account.id, "company_id": account.company_id},
                    "todo": {"filteringLines": [], "toggledSections": []},
                    "searches": {
                        "filters": {
                            "call": [],
                            "calltype": [],
                            "date": [],
                            "line": [],
                            "tag": [],
                            "teammate": [],
                        }
                    },
                    "callHistory": {"suggestionsQuery": ""},
                    "app": {
                        "alreadyPlayedCalls": [],
                        "hasNoiseCancellationPanelBeenSeen": False,
                    },
                    "emergencyNumbers": {"hasSkippedEmergencyAddressDialog": True},
                    "conversations": {"preferredCountryCode": "US"},
                },
                "betaSwitch": {
                    "wizardCompleted": skip_wizard,
                    "definitiveReturn": False,
                },
                "popToFront": True,
                "language": "en",
            },
            "lastUpdated": current_time,
        }
        self._set_local_storage_item(f"aircall-cache-user-{account.id}", user_data)

        self._driver.refresh()

        if skip_wizard:
            return KeyboardPage(self._driver)
        else:
            return OnboardingPage(self._driver)
