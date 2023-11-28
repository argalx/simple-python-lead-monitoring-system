import json

# File Location
fileLocation = "D:\Documents\GitRepos\simple-python-lead-monitoring-system\json-file\lead.json"

# Lead Object
class Lead:
    def __init__(self, name, phoneNumber, email):
        self._name = name
        self._phoneNumber = phoneNumber
        self._email = email

    def add(self):
        # Lead entry input
        name = self._name
        phoneNumber = self._phoneNumber
        email = self._email
        leadContent = self.view()

        leadEntry = {"name": name, "phoneNumber": phoneNumber, "email": email}

        # Initialize JSON file
        with open(fileLocation, "r+") as lead:

            # Append JSON file with new entry
            leadContent["leads"].append(leadEntry)

            # Pointer start at 0
            lead.seek(0)

            # Rewrite JSON file with updated entry
            json.dump(leadContent, lead)

        return "Lead added."

    def view(self):
            
        # Initialize JSON file
        with open(fileLocation, "r") as lead:

            # Loads JSON file content
            leadContent = json.load(lead)

            return leadContent

# Welcome Message
print("Welcome to Simple Python Lead Monitoring System")

# User Action Logic
while True:
    try:
        userInput = int(input("Menu: (1) Add Lead, (2) View Lead, (3) Exit Program: "))

        if userInput == 1:
            # Lead entry input
            name = input("Enter name: ")
            phoneNumber = int(input("Enter phone number: "))
            email = input("Enter email address: ")

            # Initialize Lead Instace
            lead = Lead(name, phoneNumber, email)
            
            # Call add method from Lead Instace
            print(lead.add())

        elif userInput == 2:
            
            # Initialize Lead Instance
            lead = Lead("name", "phoneNumber", "email")

            # Call view method from Lead Instance
            print(lead.view())

        elif userInput == 3:
            break
        else:
            print("Invalid input.")

    except ValueError:
        print("Invalid input.")