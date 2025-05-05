# Define a class named Person
class Person:
  # Constructor method to initialize the object with name and age
  def __init__(self, name, age):
    self.name = name  # Set the name attribute
    self.age = age    # Set the age attribute

# Create an instance (object) of the Person class with name "prince" and age 20
p1 = Person("prince", 20)

# Print the name and age using formatted string
print("my name is", p1.name)  # Output: my name is prince
print("my age is", p1.age)    # Output: my age is 20

# Print the name and age directly
print(p1.name)  # Output: prince
print(p1.age)   # Output: 20
