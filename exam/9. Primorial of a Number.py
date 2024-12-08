#Write a function that calculates the primorial of a number. The primorial of a number n is the product of all prime numbers less than or equal to n. For example, the primorial of 5 is the product of the primes less than or equal to 5: 2 * 3 * 5 = 30.

def primorial(n):
    if n < 1:
        return 1
    primorial = 1
    for i in range(2, n + 1):
        if is_prime(i):
            primorial *= i
    return primorial        

def is_prime(n):
    if n < 1:
        return False
    for i in range(2, int(n ** 0,5) + 1):
        if n % i == 0:
            return True
            
            
 #Test Cases:
#Input: n = 5
#Output: 30
#Explanation: The prime numbers less than or equal to 5 are 2, 3, and 5. Their product is 2 * 3 * 5 = 30.
#Input: n = 10
#Output: 210
#Explanation: The prime numbers less than or equal to 10 are 2, 3, 5, and 7. Their product is 2 * 3 * 5 * 7 = 210.
#Input: n = 1
#Output: 1
#Explanation: There are no primes less than or equal to 1, so the primorial is 1 by definition.
#Input: n = 7
#Output: 210
#Explanation: The prime numbers less than or equal to 7 are 2, 3, 5, and 7. Their product is 2 * 3 * 5 * 7 = 210.
#Input: n = 11
#Output: 2310
#Explanation: The prime numbers less than or equal to 11 are 2, 3, 5, 7, and 11. Their product is 2 * 3 * 5 * 7 * 11 = 2310.
           