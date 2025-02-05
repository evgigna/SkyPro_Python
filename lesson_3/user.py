class User:

    def __init__(self, first_name, last_name):
        self.last_name = last_name
        self.first_name = first_name

    def first_Name_Print (self):
        print("My name is", self.first_name)

    def last_Name_Print(self):
        print("my surname is", self.last_name)

    def name_Surname_Print(self):
        print("name", self.first_name, "surname", self.last_name)

    