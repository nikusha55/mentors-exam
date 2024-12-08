# 3. Reverse the Order of Words in a Sentence
# Task:
# Write a function that takes a sentence and reverses the order of its words.
# Test Cases:
# Input: "Hello World" → Output: "World Hello"
# Input: "Python is great" → Output: "great is Python"
# Input: "a b c" → Output: "c b a"
# Input: "" → Output: ""
# Input: " Spaces " → Output: "Spaces"


def reverse_words(st):
    st = st.split(' ')
    
    return ' '.join(st[::-1])

print(reverse_words('Python is great'))