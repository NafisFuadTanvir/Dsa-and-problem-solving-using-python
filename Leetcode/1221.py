def balancedStringSplit(s):
    R_count=0
    L_count=0
    RL_count=0

    for i in s:
        if i=="R":
            R_count+=1
        if i=="L":
            L_count+=1
        if R_count==L_count:
            RL_count+=1

    return RL_count             


print(balancedStringSplit("LLLLRRRR"))