#multiple argument passing in single parameter

def all(*args):
    for i in args:
        print(i*2)


all(10,20,30)
