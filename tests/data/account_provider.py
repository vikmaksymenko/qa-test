import threading
import os

from tests.data.account import Account
from tests.utils.utils import load_json

class AccountProvider: 
    """
    Singleton class to provide accounts for the tests

    ...

    Attributes
    ----------
    __instance : AccountProvider
        Singleton instance of the class

    __lock : threading.Lock
        Lock to synchronize the access to the singleton instance

    __accounts : dict
        Dictionary of accounts

    Methods
    -------
    get_instance() -> AccountProvider
        Gets the singleton instance of the class
    get_account(name: str) -> Account
        Gets an account by name
    __init__()
        Virtually private constructor
    __load_accounts(path_to_file: str) -> dict
        Loads accounts from a file

    """

    __instance = None
    __lock = threading.Lock()


    @staticmethod
    def get_instance():
        """ Static access method. """
        if AccountProvider.__instance == None:
            with AccountProvider.__lock:
                if AccountProvider.__instance == None:
                    AccountProvider()
        return AccountProvider.__instance


    def __init__(self):
        """ Virtually private constructor. """
        if AccountProvider.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            AccountProvider.__instance = self
            # TODO: load path to file from config 
            self.__accounts = self.__load_accounts(os.getenv('PHONE_ACCOUNTS_FILE'))

    def get_account(self, name: str) -> Account:
        """
        Get account by name

        Parameters
        ----------
        name : str
            Name of the account

        Returns
        -------
        Account
            Account object
        """
        return self.__accounts[name]
    
    def __load_accounts(self,path_to_file: str) -> dict:
        """
        Load accounts from a file

        Parameters
        ----------
        path_to_file : str
            Path to the JSON file containing the accounts

        Returns
        -------
        dict
        """
        data = load_json(path_to_file)
        result = {}
        for name, account in data.items():
            result[name] = Account(**account)
        return result