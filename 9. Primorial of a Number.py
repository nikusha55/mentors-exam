# 9. Primorial of a Number
# Task:
# Write a function that calculates the primorial of a number. The primorial of a number n is the product of all prime numbers less than or equal to n. For example, the primorial of 5 is the product of the primes less than or equal to 5: 2 * 3 * 5 = 30.
# Your function should take an integer n and return the primorial of that number.
# Test Cases:
# Input: n = 5
# Output: 30
# Explanation: The prime numbers less than or equal to 5 are 2, 3, and 5. Their product is 2 * 3 * 5 = 30.
# Input: n = 10
# Output: 210
# Explanation: The prime numbers less than or equal to 10 are 2, 3, 5, and 7. Their product is 2 * 3 * 5 * 7 = 210.
# Input: n = 1
# Output: 1
# Explanation: There are no primes less than or equal to 1, so the primorial is 1 by definition.
# Input: n = 7
# Output: 210
# Explanation: The prime numbers less than or equal to 7 are 2, 3, 5, and 7. Their product is 2 * 3 * 5 * 7 = 210.
# Input: n = 11
# Output: 2310
# Explanation: The prime numbers less than or equal to 11 are 2, 3, 5, 7, and 11. Their product is 2 * 3 * 5 * 7 * 11 = 2310.


def primorial(n):
    # create a variable of results
    result = 1
    # check each number from 2 to n
    for i in range(2, n + 1):
        prime = True
        for x in range(2, i):
            # check number of prime numbers
            if i % x == 0:
                prime = False
                break
        if prime:
            result *= i
    # return the result
    return result


print(primorial(5))  
print(primorial(10))  
print(primorial(1))  
print(primorial(7))   
print(primorial(11)) 