class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def firstname_print(self):
        print('Имя', self.first_name)

    def lastname_print(self):
        print('Фамилия', self.last_name)

    def user_print(self):
        print('Имя и Фамилия', self.first_name, self.last_name)