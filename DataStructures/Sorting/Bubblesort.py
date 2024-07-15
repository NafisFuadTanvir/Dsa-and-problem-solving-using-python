
def Bubble_sort(d):
    length_of_data= len(d)
    
    for i in range(length_of_data):
        inner_index_length= length_of_data-i-1
        
        for j in range(inner_index_length):
            
            if d[j]>d[j+1]:
                
                temp= d[j]
                d[j]= d[j+1]
                d[j+1]= temp
    return d;            




data=[100,500,-90,10,20,5]

print(Bubble_sort(data))

