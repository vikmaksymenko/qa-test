from tests.pages.phone.incall import InCallPage
from tests.pages.phone.phone_base import BasePhonePage
from tests.utils.time_utils import TimeUtils


class OnboardingPage(BasePhonePage):
    """
    Onboarding page of the phone app

    ...

    Methods
    -------
    skip_onboarding(id: int, company_id: int) -> InCallPage
        Skips the onboarding by setting the local storage item

    """

    def __init__(self, driver) -> None:
        BasePhonePage.__init__(self, driver)
        self._endpoint = "/onboarding"

    def skip_onboarding(self, id, company_id) -> InCallPage:
        """
        Skips the onboarding by setting the local storage item

        Parameters
        ----------

        id : int
            User id
        company_id : int
            Company id

        Returns
        -------
        InCallPage
        """

        user_data = {
            "data": {
                "state": {
                    "auth": {"strategy": "password"},
                    "user": {"id": id, "company_id": company_id},
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
                "betaSwitch": {"wizardCompleted": True, "definitiveReturn": False},
                "popToFront": True,
                "language": "en",
            },
            "lastUpdated": TimeUtils.current_time_milis(),
        }

        self._set_local_storage_item(f"aircall-cache-user-{id}", user_data)
        self._driver.refresh()
        return InCallPage(self._driver)
