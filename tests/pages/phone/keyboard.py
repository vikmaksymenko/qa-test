from tests.pages.base import BasePage
from tests.pages.phone.ringing import RingingPage
from tests.pages.phone.phone_base import BasePhonePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.utils.timeouts import Timeouts


class KeyboardPage(BasePhonePage):

    """Keyboard page"""

    def __init__(self, driver) -> None:
        BasePhonePage.__init__(self, driver)
        self._endpoint = "/keyboard"

        self._keyboard_input = (By.CSS_SELECTOR, "[data-test='keyboard-input-text']")
        self._dial_button = (By.CSS_SELECTOR, "[data-test='keyboard-button-dial']")

    def wait_for_page_to_load(self, timeout=Timeouts.PAGE_LOAD()) -> BasePage:
        """
        Wait for the page to load and the keyboard input to be visible
        """
        super().wait_for_page_to_load(timeout)
        WebDriverWait(self._driver, Timeouts.ELEMENT_VISIBILITY()).until(
            EC.visibility_of_element_located(self._keyboard_input)
        )
        return self

    def call_to(self, number_or_name: str) -> RingingPage:
        """
        Call to a number using the keyboard

        Parameters
        ----------
        number_or_name : str
            Number or name to call to

        Returns
        -------
        RingingPage
        """

        self._driver.find_element(*self._keyboard_input).send_keys(number_or_name)

        WebDriverWait(self._driver, Timeouts.ELEMENT_VISIBILITY()).until(
            EC.visibility_of_element_located(self._dial_button)
        )

        self._driver.find_element(*self._dial_button).click()
        return RingingPage(self._driver)
