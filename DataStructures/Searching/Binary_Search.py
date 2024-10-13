mylst=[20,30,40,50,60,70,80,90,100]  #datas must be sort asending or desending

target_value=80

start= 0
end=len(mylst)-1

while start<=end:
    
    mid_value= (start+end)//2
    
    if mylst[mid_value]== target_value:
        print(f"value exist, the value index is:- {mid_value}")
        break
    
    elif mylst[mid_value]<target_value:
        start=mid_value+1
    
    elif mylst[mid_value]>target_value:
        end= mid_value-1
            
        
    