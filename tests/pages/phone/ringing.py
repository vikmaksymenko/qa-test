from tests.pages.phone.phone_base import BasePhonePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.utils.timeouts import Timeouts


class RingingPage(BasePhonePage):

    """Ringing page"""

    def __init__(self, driver) -> None:
        BasePhonePage.__init__(self, driver)
        self._endpoint = "/ringing"

        self._hangup_button = (By.CSS_SELECTOR, "[data-test='hangup-button']")
        self._pickup_button = (By.CSS_SELECTOR, "[data-test='pickup-button']")
        self._participant_phone_number = (
            By.CSS_SELECTOR,
            "[data-test='participant-phone-number']",
        )
        self._contact_name = (By.CSS_SELECTOR, "[data-test='contact-name']")

    def wait_for_page_to_load(self, timeout=Timeouts.PAGE_LOAD()) -> "RingingPage":
        """
        Wait for the page to load and the hangup button to be visible
        In fact, the timeout is doubled here, but I haven't found a better way to do it
        """

        super().wait_for_page_to_load(timeout)
        WebDriverWait(self._driver, Timeouts.ELEMENT_VISIBILITY()).until(
            EC.visibility_of_element_located(self._hangup_button)
        )

    def should_have_contact_name(self, name: str) -> "RingingPage":
        """
        Assert that the contact name is the expected one
        """

        contact_name = self._driver.find_element(*self._contact_name).text.replace(
            " ", ""
        )
        assert contact_name == name
        return self
