class Animal:
    def __init__(self, name, specie):
        self.name = name
        self.specie = specie

    def make_sound(self):
        print("Generic sound of the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        # Call the constructor from the parent class to initialize inherited attributes
        super().__init__(name, "Dog")
        self.breed = breed

    def make_sound(self):
        print("Guau!")

# Create instances
my_dog = Dog("Bobby", "Beagle")
my_animal = Animal("Generic", "unknown")

# Call method
my_dog.make_sound()  # Print: Guau!
my_animal.make_sound()  # Print: Generic sound of the animal

# Access to attributes
print(my_dog.name)  # Print: Bobby
print(my_dog.breed)  # Print: Beagle
print(my_dog.specie)  # Print: Dog