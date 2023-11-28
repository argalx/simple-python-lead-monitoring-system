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
    try:
        userInput = int(input("Menu: (1) Add Lead, (2) View Lead, (3) Exit Program: "))

        if userInput == 1:
            pass
        elif userInput == 2:
            pass
        elif userInput == 3:
            break
        else:
            print("Invalid input.")

    except ValueError:
        print("Invalid input.")
    