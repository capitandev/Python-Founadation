
print("----- What is Class -----")

# Class - Blueprint for object creation
# Structure: State + Constructor + Methods


class Person:

    # Static property (Class property)
    message = "Class state property"

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Ordinary method
    def introduce(self):
        print(f"{self.name} says: How do you do!")

    def say_age(self):
        print(f"{self.name} says: I am {self.age}")


# Creating objects
person1 = Person("Justin", 25)
person2 = Person("Ali", 15)
person3 = Person("Alex", 35)


# Ordinary properties
print("person1.name:", person1.name)
print("person2.name:", person2.name)

# Ordinary methods
person1.introduce()
person2.say_age()

# Static property
print(Person.message)

print("--------- End ---------")
