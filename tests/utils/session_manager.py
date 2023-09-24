from selenium import webdriver


class SessionManager:
    """
    Class to manage sessions.

    ...

    Attributes
    ----------
    _sessions : dict
        Dictionary to store sessions

    Methods
    -------
    add(name: str, session: RemoteDriver) -> None
        Adds a session to the dictionary
    get(name: str) -> RemoteDriver
        Gets a session from the dictionary
    quit() -> None
        Quits all sessions
    """

    def __init__(self) -> None:
        self._sessions = {}

    def add(self, name: str, session: webdriver.Remote) -> None:
        """
        Adds a session to the dictionary

        Parameters
        ----------
        name : str
            name of the session
        session : RemoteDriver
            session to add
        """
        self._sessions[name] = session

    def get(self, name: str) -> webdriver.Remote:
        """
        Gets a session from the dictionary

        Parameters
        ----------
        name : str
            name of the session

        Returns
        -------
        webdriver.Remote

        Raises
        ------
        Exception
            If session not found
        """

        if name not in self._sessions:
            raise Exception(f"Session {name} not found")
        return self._sessions[name]

    def quit(self) -> None:
        """Quits all sessions"""

        for session in self._sessions.values():
            session.quit()
        self._sessions = {}
