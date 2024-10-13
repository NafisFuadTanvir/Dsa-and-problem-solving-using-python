def categorize_temperature(temp):
    if temp<10 or temp>25:
        if temp<10:
             return "cold"
        else:
            return "hot"
       
        
    else:
        return "warm"
    

print(categorize_temperature(11.5)) 