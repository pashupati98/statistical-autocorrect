import os
import re
import numpy as np
import pandas as pd
from collections import Counter
import nltk

# Reading the data

with open('./data/shakespeare.txt', 'r') as f:
    file = f.readlines()


def process_data(lines):
    """
    Input:
        A file_name which is found in your current directory. You just have to read it in.
    Output:
        words: a list containing all the words in the corpus (text file you read) in lower case.
    """
    words = []
    for line in lines:
        line = line.strip().lower()
        word = re.findall(r'\w+', line)
        words.extend(word)

    return words


# Check word list
word_l = process_data(file)
vocab = set(word_l)
print(f"The first ten words in the text are: \n{word_l[0:10]}")
print(f"There are {len(vocab)} unique words in the vocabulary.")

