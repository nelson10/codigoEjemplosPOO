class Animal1:
    def speak(self):
        print("Some sound")

class Cat(Animal1):
    pass
    #def speak(self):
    #    print("Meow")
c = Cat()
c.speak() # Meow