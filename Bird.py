class Bird:
    def make_sound(self):
        print("Chirp")

class Duck:
    def make_sound(self):
        print("Quack")

def animal_sound(animal):
    animal.make_sound()

bird = Bird()
duck = Duck()
animal_sound(bird) # Chirp
animal_sound(duck) # Quack