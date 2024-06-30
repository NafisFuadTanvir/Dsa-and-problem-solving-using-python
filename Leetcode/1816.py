def truncateSentence( s, k):
        splitted_string=s.split()
        return " ".join(splitted_string[0:k]) 


print(truncateSentence(s = "Hello how are you Contestant", k = 4))