#A child class inherits from more than one parent class.

class mother:
    def __init__(self,mother_name):
        self.mother_name=mother_name

    def introduce_mother(self):
        return f"{self.mother_name} is my mother"

class father:
    def __init__(self,father_name):
        self.father_name= father_name

    def introduce_father(self):
        return f"{self.father_name} is my father"    
        
class child(mother,father):
    def __init__(self, mother_name, father_name):
        mother.__init__(self, mother_name)
        father.__init__(self, father_name)


child1=child("nargis are begum","Mohammad abdul khalek")

print(child1.introduce_father())
print(child1.introduce_mother())
