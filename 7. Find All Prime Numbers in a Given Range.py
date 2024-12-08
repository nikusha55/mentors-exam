# 7. Find All Prime Numbers in a Given Range
# Task:
# Write a function that takes two integers, start and end, and returns a list of all prime numbers in the range [start, end]. A prime number is a number greater than 1 that has no divisors other than 1 and itself.
# Test Cases:
# Input: start = 10, end = 20
# Output: [11, 13, 17, 19]
# Input: start = 1, end = 10
# Output: [2, 3, 5, 7]
# Input: start = 20, end = 30
# Output: [23, 29]
# Input: start = 24, end = 25
# Output: []
# Input: start = 1, end = 1
# Output: []




def find_primes(start, end):
    prims = []
    ls = []
    for i in range(start, end):
        ls.append(i)
    
    for i in ls:
        if i > 1:
            prime = True
            for x in range(2, i):
                if i % x == 0:
                    prime = False
                    break
            if prime:
                prims.append(i)
    
    return prims

print(find_primes(10, 20))
print(find_primes(1, 10))
print(find_primes(20, 30))
print(find_primes(24, 25))
print(find_primes(1, 1))