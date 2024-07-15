numberOfElements= int(input())

lst=[]

for i in range(numberOfElements):
    num=int(input())
    lst.append(num)

for number in lst:
    if number<=120:
        if number%10==0:
            print(number)
            
    else:
        break            