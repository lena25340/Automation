class User:

    def __init__(self, first_name, last_name):
        self.Name = first_name
        self.last = last_name

    def sayName(self):
        print(self.Name)

    def saylast_name(self):
        print(self.last)

    def sayfirstlast_name(self):
        print(self.Name, self.last)