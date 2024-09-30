#[20,30,40,50,60]


def insertion_sort(lst):
    leng= len(lst)
    
    for i in range(1,leng): #[30---to ---60]
        key_index=lst[i] #index 1 means value--->30
        perv_index= i-1  #prev index value 1-1=0--->20
        
        while perv_index>=0 and key_index<lst[perv_index]:
            lst[perv_index+1]= lst[perv_index]
            perv_index=perv_index-1
            
        
        lst[perv_index+1]=key_index
        print(lst)
            
            

mylist=[50,40,35,2,6,8]   

insertion_sort(mylist)         
        
        