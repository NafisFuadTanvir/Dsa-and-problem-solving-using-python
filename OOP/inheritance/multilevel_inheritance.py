class grandparent:
    def __init__(self,name):
        self.name=name

    def display(self):
        return f" my grandpa's name is {self.name}"


class parent(grandparent):
    def __init__(self):
        pass



class child(parent):
    def __init__(self):
        pass



nafis= child()

print(nafis.display())







