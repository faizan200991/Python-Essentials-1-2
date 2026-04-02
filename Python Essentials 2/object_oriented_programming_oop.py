"""PE2 Topic 5: Object-Oriented Programming (OOP)"""


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self._breed = breed  # protected-style attribute by convention

    def speak(self):
        return "Woof!"

    def get_breed(self):
        return self._breed


pet = Dog("Buddy", "Labrador")
print(pet.name, "says", pet.speak())
print("Breed:", pet.get_breed())
