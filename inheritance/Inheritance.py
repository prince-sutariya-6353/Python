# Parent class
class Animal:
    def __init__(self, name):
        # Initialize the animal with a name
        self.name = name

    def speak(self):
        # Generic speak method for an animal
        print(f"{self.name} makes a sound")

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        # Override speak method for Dog
        print(f"{self.name} barks")

# Another child class inheriting from Animal
class Cat(Animal):
    def speak(self):
        # Override speak method for Cat
        print(f"{self.name} meows")

# Using the classes
dog = Dog("Buddy")       # Create a Dog object named Buddy
cat = Cat("Whiskers")    # Create a Cat object named Whiskers

dog.speak()  # Output: Buddy barks
cat.speak()  # Output: Whiskers
