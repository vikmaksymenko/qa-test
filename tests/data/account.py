class Account:
    """Account data class

    Attributes:
    -----------
    _email : str
        email of the account
    _password : str
        password of the account
    _phone : str
        phone of the account
    _id : int
        id of the account
    _company_id : int
        company id of the account

    Methods:
    --------
    email() -> str
        Returns email of the account
    password() -> str
        Returns password of the account
    phone() -> str
        Returns phone of the account
    id() -> int
        Returns id of the account
    company_id() -> int
        Returns company id of the account
    """

    def __init__(self, email: str, password: str, phone: str, id: int = 0, company_id: int = 0):
        self._email = email
        self._password = password
        self._phone = phone
        self._id = id
        self._company_id = company_id

    @property
    def email(self) -> str:
        return self._email

    @property
    def password(self) -> str:
        return self._password

    @property
    def phone(self) -> str:
        return self._phone

    @property
    def id(self) -> int:
        return self._id

    @property
    def company_id(self) -> int:
        return self._company_id
