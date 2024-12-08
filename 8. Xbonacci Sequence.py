# 8. Xbonacci Sequence
# Task:
# Write a function that generates the Xbonacci sequence. The Xbonacci sequence is a generalization of the Fibonacci sequence, where each number is the sum of the previous X numbers in the sequence.
# For example, if X = 3 and the initial sequence is [1, 1, 1], the sequence will proceed as follows:
# The 4th number is the sum of the previous 3: 1 + 1 + 1 = 3.
# The 5th number is the sum of the previous 3: 1 + 1 + 3 = 5.
# The 6th number is the sum of the previous 3: 1 + 3 + 5 = 9.
# Your function should take two arguments:
# X: The number of previous terms to sum.
# n: The number of terms to generate.
# Test Cases:
# Input: X = 3, n = 10
# Output: [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
# Explanation: The first 10 numbers of the Xbonacci sequence starting with [1, 1, 1] and X = 3.
# Input: X = 2, n = 10
# Output: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# Explanation: This is the Fibonacci sequence, where each number is the sum of the previous two numbers.
# Input: X = 4, n = 6
# Output: [1, 1, 1, 1, 4, 7]
# Explanation: Starting with [1, 1, 1, 1], the next terms are calculated by summing the last 4 terms.
# Input: X = 5, n = 8
# Output: [1, 1, 1, 1, 1, 5, 9, 17]
# Explanation: The sequence starts with five 1s, and each subsequent number is the sum of the previous 5 numbers.
# Input: X = 3, n = 1
# Output: [1]
# Explanation: Only one term in the sequence is required, so the output is [1].

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


def xbonacci(X, n):
    sequence = [1] * X
    for i in range(X, n):
        sequence.append(sum(sequence[i-X:i]))
    return sequence[:n]

print(xbonacci(3, 10))  
print(xbonacci(2, 10))  
print(xbonacci(4, 6))   
print(xbonacci(5, 8))   
print(xbonacci(3, 1))   