def isValid( s):
    pair_paranthesis={   
      "(": ")",
      "{": "}",
      "[": "]"
    }
    stack=[]
    for ch in s:
        if ch in pair_paranthesis.keys():
            stack.append(ch)
        else:
            if not stack:
                return False
            else:
             peek_paranthesis= stack.pop()
            
             if pair_paranthesis[peek_paranthesis]!=ch:
                return False
            

    if stack:
        return False
    return True                
        
print(isValid("()){}}"))        
