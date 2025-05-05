class Animal:
    def sound(self):
        print("This animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog says: Woof!")

class Cat(Animal):
    def sound(self):
        print("Cat says: Meow!")

# Function that uses polymorphism
def make_sound(animal):
    animal.sound()

# Create objects
a = Animal()
d = Dog()
c = Cat()

# Call the same function with different types
make_sound(a)  # This animal makes a sound
make_sound(d)  # Dog says: Woof!
make_sound(c)  # Cat says: Meow!
