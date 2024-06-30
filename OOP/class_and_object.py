class person:
    #constructor
    def __init__(self,name,age):
        self.name=name
        self.age=age
        #method
    def introduce(self):

        return f"i am {self.name} and i am {self.age} years old"
          
person1 =person("nafis fuad tanvir",18)
person2= person("torikul islam tamim",11)

print(person1.introduce())
print(person2.introduce())