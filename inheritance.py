class Animal:
    def __init__(self, name):
        self.name = name


    def speak(self):
        print("Some animal sound")

class Dog(Animal):
    def speak(self):
        super().speak()
        print(f"Woof! My name is {self.name}")

animal1 = Animal("cat")
animal1.speak()

dog1 = Dog("Rex")
dog1.speak()


