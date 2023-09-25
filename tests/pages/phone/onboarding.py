from tests.pages.phone.phone_base import BasePhonePage

class OnboardingPage(BasePhonePage):
    """
    Onboarding page of the phone app
    """

    def __init__(self, driver) -> None:
        BasePhonePage.__init__(self, driver)
        self._endpoint = "/onboarding"
