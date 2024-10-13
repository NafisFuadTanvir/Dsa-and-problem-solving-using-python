def analyze_ratings(ratings):
    
    
    min_rating= ratings[0] # [0]
    max_rating= ratings[0] #[0]
    
    for rating in ratings:
        if rating< min_rating: 
            min_rating=rating
        
        elif rating>max_rating :
            max_rating=rating
    
    return [min_rating,max_rating]
    
    
    
mylist=[1,5,8,6,7]

print(analyze_ratings(mylist))