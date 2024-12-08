#Write a function that takes a sentence and reverses the order of its words.
def reverse_words(sentence):
    words=sentence.split()
    reverse_words=words[::-1]
    reversed_sentence= " ".join(reverse_words)
    return reversed_sentence


#Test Cases:
#Input: "Hello World" → Output: "World Hello"
#Input: "Python is great" → Output: "great is Python"
#Input: "a b c" → Output: "c b a"
#Input: "" → Output: ""
#Input: " Spaces " → Output: "Spaces"
