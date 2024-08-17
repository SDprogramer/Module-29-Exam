class Animal:
    def make_sound(self):
        pass # This method will be overridden
    
class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

dog = Dog()
dog.make_sound()
cat = Cat()
cat.make_sound()