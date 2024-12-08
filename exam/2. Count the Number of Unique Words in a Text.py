#Write a function that counts the number of unique words in a string, ignoring case sensitivity and punctuation.



import string

def count_unique_words(text):
    #გადავიყვანოთ პატარა ასოებში და ამოვიღოთ პუნქტუაცია
    text=text.lower()
    text=text.translate(str.maketrans("", "", string.punctuation))
    
    #გავყოთ ტექსტი სიტყვებად და მოვძებნოთ უნიკალური სიტყვები
    words=text.split()
    unique_words =set(words)
    
    
    #Test Cases:
#Input: "The quick brown fox jumps over the lazy dog" → Output: 8
#Input: "Hello hello world!" → Output: 2
#Input: "" → Output: 0
#Input: "Python is fun. Python is cool." → Output: 4
#Input: "One word" → Output: 2

    