import json
import os
from time import sleep

# clear interpreter variable
clear = lambda: os.system('cls')

# File Location
fileLocation = "D:\Documents\GitRepos\simple-python-lead-monitoring-system\json-file\lead.json"

# Lead Object
class Lead:
    def __init__(self, name, phoneNumber, email):
        self._name = name
        self._phoneNumber = phoneNumber
        self._email = email

    # Adding data to JSON file
    def add(self):
        # Lead entry input
        name = self._name
        phoneNumber = self._phoneNumber
        email = self._email
        leadContent = self.load()

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

    # Loading raw data from JSON file
    def load(self):
        # Initialize JSON file
        with open(fileLocation, "r") as lead:

            # Loads JSON file content
            leadContent = json.load(lead)

        return leadContent
    
    # Printing formatted JSON file content
    def print(self):
        leadContent = self.load()
        # Lead entry counter
        objectCount = 0

        # Lead entry header
        print(f"{'Name':<25}{'Phone Number':^20}{'Email Address':>25}")

        # Format Lead entry
        for object in leadContent["leads"]:
            print(f"{object['name']:<25}{object['phoneNumber']:^20}{object['email']:>25}")
            objectCount += 1

        # Lead entry total count
        print(f"Total Entry: {objectCount}")

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
            lead.print()
        elif userInput == 3:
            print("Exiting program...")
            break
        else:
            print("Invalid input.")

    except ValueError:
        print("Invalid input.")

    # Pause for n seconds after printing output
    sleep(5)

    # Clear screen for windows only
    clear()