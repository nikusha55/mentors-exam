# 2.CounttheNumberofUniqueWordsinaText
#  Task:
#  Writeafunctionthatcountsthenumberofuniquewordsinastring, ignoringcasesensitivity
#  andpunctuation.
#  TestCases:
# Input: "The quick brown fox jumps over the lazy dog" → Output: 8
# Input: "Hello hello world!" → Output: 2
# Input: "" → Output: 0
# Input: "Python is fun. Python is cool." → Output: 4
# Input: "One word" → Output: 2


def count_num(strng):
    count = 0
    clear = '.[]!,'
    word = ''
    for i in strng:
        if i not in clear:
            word = word + i
    
    words = word.lower().split()

    unical_words = set(words)

    return len(unical_words)

print(count_num("One word"))