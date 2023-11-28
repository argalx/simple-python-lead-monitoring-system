# Lead Object
class Lead:
    def __init__(self, name, phoneNumber, email):
        self._name = name
        self._phoneNumber = phoneNumber
        self._email = email

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        pass

    @property
    def phoneNumber(self):
        return self._phoneNumber

    @phoneNumber.setter
    def phoneNumber(self, value):
        pass

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        pass