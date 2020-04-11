class User():
    def __init__(self, first, last, phone):
        self.first = first
        self.last = last
        self.phone = phone
        self.email = first + "." + last + "@company.gr"
    
    def describeUser(self):
        print("Users first name is: " + self.first.title())
        print("Users last name is: " + self.last.title())
        print("Users phone is: " + self.phone.title())
        print("Users email is: " + self.email.title())

    def greetUser(self):
        print("Hello " + self.first.title() + " how are you?")

dimitris = User("Dimitris", "Dim", "+30303030300")
antreas = User("Antreas", "Dim", "+30003003003")


dimitris.describeUser()
dimitris.greetUser()
print("\n")
antreas.describeUser()
antreas.greetUser()