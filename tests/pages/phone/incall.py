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
    
    def click_action_button(self, name: str) -> "InCallPage":
        """
        Click on a button

        Parameters
        ----------
        name : str
            Name of the button

        Returns
        -------
        InCallPage
        """
        name = name.lower().replace(" ", "-")
        self._driver.find_element(By.CSS_SELECTOR, f"[data-test='action-{name}']").click()
        return self
    
    def should_have_action_button(self, name: str) -> "InCallPage":
        """
        Assert that the page has a button

        Parameters
        ----------
        name : str
            Name of the button

        Returns
        -------
        InCallPage
        """
        name = name.lower().replace(" ", "-")
        WebDriverWait(self._driver, Timeouts.ELEMENT_VISIBILITY()).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, f"[data-test='action-{name}']"))
        )
        return self