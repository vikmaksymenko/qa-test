from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

class SessionProvider:
    """
    Class to provide sessions for tests. 
    In current implementation it creates only a chrome session, 
    however it can be extended to provide other types of sessions for mobile and desktop apps
    
    ...

    Methods
    -------

    init_chrome_session() -> webdriver.Remote
        Creates a chrome session.
    """


    @staticmethod
    def init_chrome_session() -> webdriver.Remote:
        """
        Creates a chrome session.

        Returns
        -------
        webdriver.Remote
        """
        options = ChromeOptions()
        options.add_argument("--use-fake-device-for-media-stream")
        options.add_argument("--use-fake-ui-for-media-stream")
        options.add_experimental_option("useAutomationExtension", False)
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_experimental_option(
            "prefs", {"profile.default_content_setting_values.notifications": 2}
        )

        return webdriver.Remote(
            command_executor="http://localhost:4444",  # TODO: Get this from ENV
            options=options,
        )
