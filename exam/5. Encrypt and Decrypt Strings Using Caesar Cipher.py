#Write a function to encrypt strings using a Caesar cipher with a given shift value.

def caesar_cipher(text, shift):
    result=''
    for char in text:
        if char.isalpha():
            start=ord('a') if char.islower() else ord('A')
            shifted_char=chr((ord(char)- start + shift) % 26 + start)
        else:
            shifted_char=char
    return result           


#Test Cases:
#Input: ("abc", 2) → Output: "cde"
#Input: ("xyz", 3) → Output: "abc"
#Input: ("Hello, World!", 5) → Output: "Mjqqt, Btwqi!"
#Input: ("Python", 0) → Output: "Python"
#Input: ("abc", -1) → Output: "zab"
