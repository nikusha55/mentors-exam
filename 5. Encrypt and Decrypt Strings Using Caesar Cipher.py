# 5. Encrypt and Decrypt Strings Using Caesar Cipher
# Task:
# Write a function to encrypt strings using a Caesar cipher with a given shift value.
# Test Cases:
# Input: ("abc", 2) → Output: "cde"
# Input: ("xyz", 3) → Output: "abc"
# Input: ("Hello, World!", 5) → Output: "Mjqqt, Btwqi!"
# Input: ("Python", 0) → Output: "Python"
# Input: ("abc", -1) → Output: "zab"


def caesar_cipher_encrypt(strng, num):
    result = ""
    is_lower = 'abcdefghijklmnopqrstuvwxyz'  
    is_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  

    for i in strng:
        if i in is_lower:
            index = is_lower.index(i)
            index1 = (index + num) % 26  
            result += is_lower[index1]
        elif i in is_upper:
            index = is_upper.index(i)
            index1 = (index + num) % 26 
            result += is_upper[index1]
        else:
            result += i  
    
    return result


print(caesar_cipher_encrypt("abc", 2))       
print(caesar_cipher_encrypt("xyz", 3))       
print(caesar_cipher_encrypt("Python", 0))     
print(caesar_cipher_encrypt("abc", -1))      
 