def even(num):
    evens = [n for n in num if n % 2 == 0]
    return sorted(evens, reverse=True)

print(even([3, 10, 4, 7, 2, 15])) 
