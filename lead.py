# Lead Object
class Lead:
    def __init__(self, name, phoneNumber, email):
        self._name = name
        self._phoneNumber = phoneNumber
        self._email = email

    def add(self):
        pass

    def view(self):
        pass

# Welcome Message
print("Welcome to Simple Python Lead Monitoring System")

# User Action Logic
while True:
    userInput = int(input("Options: (1) Add Lead, (2) View Lead, (3) Exit Program"))

    
    