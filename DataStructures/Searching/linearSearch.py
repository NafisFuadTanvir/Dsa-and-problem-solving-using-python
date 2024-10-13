
def linear_search(ls,value):
    
    for i in ls:
        if i==value:
           return True
            
    return False    


myls=[10,20,50,60,70,5,2]

value=60 

print(linear_search(myls,value))   