from tests.pages.phone.phone_base import BasePhonePage
from .ringing import RingingPage
from tests.utils.timeouts import Timeouts

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InCallPage(RingingPage):

    """In call page"""

    def __init__(self, driver) -> None:
        RingingPage.__init__(self, driver)
        self._endpoint = "/incall"

        self._timer = (
            By.CSS_SELECTOR,
            "[data-test='incall-header'] [data-test='paragraph-text']",
        )

    def wait_for_page_to_load(self, timeout=Timeouts.PAGE_LOAD()) -> "InCallPage":
        """
        Wait for the page to load and the call timer to be visible
        """
        super().wait_for_page_to_load(timeout)
        WebDriverWait(self._driver, Timeouts.ELEMENT_VISIBILITY()).until(
            EC.visibility_of_element_located(self._timer)
        )
        return self
