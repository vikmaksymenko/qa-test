import requests


class IdApi:
    @staticmethod
    def login(email: str, password: str) -> requests.Response:
        """
        Login to AirCall

        Parameters
        ----------
        email : str
            email to login
        password : str
            password to login

        Returns
        -------
        requests.Response
            response from the API

        Raises
        ------
        RuntimeError
            If login failed
        """

        url = "https://id.aircall.io/auth/v1/users/session"
        json = {"email": email, "password": password}

        headers = {
            "Content-Type": "application/json",
        }

        response = requests.post(url, json=json, headers=headers)

        if response.status_code != 200:
            raise RuntimeError("Login failed. Status code: " + str(response.status_code)) 

        return response.json()
