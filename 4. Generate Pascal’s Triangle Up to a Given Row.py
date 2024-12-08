# 4. Generate Pascal’s Triangle Up to a Given Row
# Task:
# Write a function to generate Pascal's Triangle up to the specified number of rows.
# Test Cases:
# Input: 1 → Output: [[1]]
# Input: 2 → Output: [[1], [1, 1]]
# Input: 3 → Output: [[1], [1, 1], [1, 2, 1]]
# Input: 5 → Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
# Input: 0 → Output: []

def generate_pascals_triangle(n):
    result = []
    for i in range(n):
        row = [1] * (i + 1)
        for x in range(1, i):
            row[x] = result[i - 1][x - 1] + result[i - 1][x]
        result.append(row)
    return result

print(generate_pascals_triangle(1)) 
print(generate_pascals_triangle(2))  
print(generate_pascals_triangle(3))  
print(generate_pascals_triangle(5))  
print(generate_pascals_triangle(0))