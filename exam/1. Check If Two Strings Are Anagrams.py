#Write a function that determines if two strings are anagrams of each other.
def are_anagrams(str1, str2):
    str1 = str1.replace(" ", " ").lower()
    str2 = str2.replace(" ", " ").lower()
    return sorted(str1) == sorted(str2)


#Test Cases:
#⦁	Input: ("listen", "silent") → Output: True
#⦁	Input: ("triangle", "integral") → Output: True
#⦁	Input: ("apple", "pale") → Output: False
#⦁	Input: ("a", "a") → Output: True
#⦁	Input: ("rat", "car") → Output: False
