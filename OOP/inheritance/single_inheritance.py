#A child class inherits from a single parent class.

#base class
class animal:
    def __init__(self,name):
        self.name= name
    def speak(self):
        pass

#child class who inherite the base class
class dog(animal):
    def speak(self):
        return f"{self.name} speaks like:- geu geu"
Dog=dog("cuty")
print(Dog.speak())     



