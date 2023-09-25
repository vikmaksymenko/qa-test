import base64
import os

class ApiUtils:

    @staticmethod
    def prepare_token():
        """
        Encode token using Base64 encoding
        """
        if os.getenv('API_ID') and os.getenv('API_TOKEN'):
            return "Basic " + base64.b64encode(f"{os.getenv('API_ID')}:{os.getenv('API_TOKEN')}".encode()).decode()
        raise RuntimeError("API_ID and API_TOKEN env variables are not set")
    
