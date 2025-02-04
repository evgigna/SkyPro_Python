class User:

    def __init__(self, first_name, last_name):
        self.last_name = last_name
        self.first_name = first_name

    def firstNamePrint (self):
        print("My name is", self.first_name)

    def lastNamePrint(self):
        print("my surname is", self.last_name)

    def nameSurnamePrint(self):
        print("name", self.first_name, "surname", self.last_name)

    