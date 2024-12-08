#Write a function to generate Pascal's Triangle up to the specified number of rows.

def generate_pascal_triangle(num_rows):
    triangle= []
    for i in range(num_rows):
        row=[1] * (i + 1)
        for j in range(1, i):
          row[j] = triangle[i - 1][j - 1] + triangle[i -1][j]  
        triangle.append(row)  
    return triangle        



#Test Cases:
#Input: 1 → Output: [[1]]
#Input: 2 → Output: [[1], [1, 1]]
#Input: 3 → Output: [[1], [1, 1], [1, 2, 1]]
#Input: 5 → Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
#Input: 0 → Output: []
