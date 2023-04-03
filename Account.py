class Account:
    def __init__(self, username, password, email):
        self._username =  username
        self._password = password
        self._email = email

class Admin(Account):
    def __init__(self, username, password, email, name, id = "admin"):
        super().__init__(username, password, email)
        self.__name = name
        self.__id = id

class Customer(Account):
    def __init__(self, username, password, email, name):
        super().__init__(username, password, email)
        self.__name = name
        self.__address = []
        self.__shipping_status = []
        self.__history_purchase = []
        self.__point = []