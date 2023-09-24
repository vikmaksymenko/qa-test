from tests.pages.phone.incall import InCallPage
from tests.pages.phone.ringing import RingingPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.utils.timeouts import Timeouts


class RingingIncomingPage(RingingPage):
    """
    Ringing incoming page
    """

    def __init__(self, driver) -> None:
        RingingPage.__init__(self, driver)
        self._endpoint = "/ringing"

        self._pickup_button = (By.CSS_SELECTOR, "[data-test='pickup-button']")

    def wait_for_page_to_load(
        self, timeout=Timeouts.PAGE_LOAD()
    ) -> "RingingIncomingPage":
        """
        Wait for the page to load and the hangup button to be visible
        """
        super().wait_for_page_to_load(timeout)
        WebDriverWait(self._driver, Timeouts.ELEMENT_VISIBILITY()).until(
            EC.visibility_of_element_located(self._pickup_button)
        )
        return self

    def pickup_call(self) -> InCallPage:
        """
        Pickup the call

        Returns
        -------
        InCallPage
        """
        self._driver.find_element(*self._pickup_button).click()
        return InCallPage(self._driver)
