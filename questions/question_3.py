"""
    Dictionaries: 

    Question 3: Implement a function word_frequency(sentence) that takes 
    a sentence and returns a dictionary containing the frequency of each 
    word in the sentence. 

    Ignore punctuation and consider words in a case-insensitive manner. 

    sample input = 

    sentence = "This is a test sentence. This sentence is a test."
    result = word_frequency(sentence)
    print(result)
"""
import string
import re

def word_frequency(sentence):
    # new_sentence = sentence.translate(str.maketrans("", "", string.punctuation)).lower()
    words = re.findall(r'\b\w+\b', sentence.lower())

    word_frequency = {}

    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    return word_frequency
