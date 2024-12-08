#Write a function that takes two integers, start and end, and returns a list of all prime numbers in the range [start, end]. A prime number is a number greater than 1 that has no divisors other than 1 and itself

def find_primes(start, end):
    primes=[]
    for num in range(start, end +1):
        if num > 1:
            is_prime=True
            for i in range(2, int(num**0,5) + 1):
                if num % i ==0:
                    is_prime= False
                    break
                if is_prime:
                    primes.append(num)
    return primes                

#Test Cases:
#Input: start = 10, end = 20
#Output: [11, 13, 17, 19]
#Input: start = 1, end = 10
#Output: [2, 3, 5, 7]
#Input: start = 20, end = 30
#Output: [23, 29]
#Input: start = 24, end = 25
#Output: []
#Input: start = 1, end = 1
#Output: []


                
                    