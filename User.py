# your User class goes here
class User:
    def __init__(self, last_name, first_name, dob, license_number=None, email_address=None) -> None:
        self.last_name = last_name
        self.first_name = first_name
        self.dob = dob
        self.email_address = email_address
        self.license_number = license_number

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}" #example of composition

#without using the following str dunder method, you can only print out it's memory location
#the dunder method str is required to be able to print to the terminal corrently
    def __str__ (self) -> str:
        return f"{self.last_name} {self.first_name} {self.dob}"
    
user001 = User("Smith", "Alice","the 1800's", 123456)
user002 = User("Appleseed", "Johnny",14022001, 98765)

print(user001)
print(user002.get_full_name())

# user_001 = User("Smith", "John", "john@email.com", 1234567)
# user_002 = User("Woodard", "Debra", "dWoodard@email.com", 4523854)
# user_003 = User("Ray", "Christopher", "chris@email.com", 7812034)

# print(user_001)
# print(user_002)
# print(user_003)
