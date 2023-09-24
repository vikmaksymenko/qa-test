from tests.pages.base import BasePage
from selenium import webdriver


class BasePhonePage(BasePage):
    """
    Base class for all phone app pages.

    ...

    Attributes
    ----------
    _base_url : str
        Base url of the application: https://phone.aircall.io

    _endpoint : str
        Endpoint of the page

    _driver : webdriver.Remote
        Driver to use for the page
    """

    def __init__(self, driver: webdriver.Remote) -> None:
        BasePage.__init__(self, driver)
        self._base_url = "https://phone.aircall.io"
        self._endpoint = ""
