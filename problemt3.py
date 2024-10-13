def multiplication_table(number,range_limit):
    for i in range(1, range_limit + 1):
        multiplication_Table = number * i
        print(f"{number} x {i} = {multiplication_Table}")


multiplication_table(10, 10)