def numJewelsInStones( jewels, stones):
        count=0
        for stone in stones:
            for jewel in jewels:
                if stone==jewel:
                    count=count+1
        return count


print(numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))