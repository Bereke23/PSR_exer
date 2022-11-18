from colorama import Fore, Style

class Dog:
    def __init__(self, name, color, age, owner):
        self.name, self.color, self.age = name, color, age
        self.owner = owner
        self.brothers = []  # no brothers for now

    def addBrother(self, name):
        self.brothers.append(name)

    # When we say to print the following part of the cod is going to be activated
    def __str__(self):
        return 'name: ' + Fore.RED + str(self.name) + Fore.RESET + \
               ', age: ' + Fore.RED + str(self.age) + Fore.RESET +\
               ', color: ' + Fore.RED + str(self.color) + Fore.RESET +\
               ', owner: ' + Fore.RED + str(self.owner) + Fore.RESET + \
               ', brothers: ' + Fore.BLUE + str(self.brothers) + Style.RESET_ALL