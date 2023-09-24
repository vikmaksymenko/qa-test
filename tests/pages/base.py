from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.utils.timeouts import Timeouts


class BasePage:
    """
    Base class for all pages.

    ...

    Attributes
    ----------

    _base_url : str
        Base url of the application

    _endpoint : str
        Endpoint of the page

    _driver : webdriver.Remote
        Driver to use for the page

    Methods
    -------
    open() -> BasePage
        Opens the page
    """

    def __init__(self, driver: webdriver.Remote) -> None:
        self._driver = driver

    def open(self) -> "BasePage":
        """
        Opens the page

        Returns
        -------
        BasePage
        """

        self._driver.get(self._base_url + self._endpoint)
        return self

    def wait_for_page_to_load(self, timeout=Timeouts.PAGE_LOAD()) -> "BasePage":
        """Wait for the page to load"""
        WebDriverWait(self._driver, timeout).until(EC.url_contains(self._endpoint))
        return self

    def _set_local_storage_item(self, name: str, data) -> any:
        """
        Set an item in the local storage of the browser

        Parameters
        ----------
        name : str
            Name of the item
        data : any
            Data to store

        Returns
        -------
        any
        """

        local_storage_script = (
            f"window.localStorage.setItem('{name}', JSON.stringify(arguments[0]));"
        )
        return self._driver.execute_script(local_storage_script, data)
