import json
import re
import string

import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.util import ngrams


def calc_hash(txt, base):
    hash = 0
    for size in range(3):
        hash += ord(txt[size]) * pow(base, 2 - size)
    return hash


# function that returns the index at which minimum value of a given list (window) is located
def minIndex(arr):
    minI = 0
    minV = arr[0]
    n = len(arr)
    for i in range(n):
        if arr[i] <= minV:
            minV = arr[i]
            minI = i
    return minI


def data_processing(text, winSize=4):
    # removing numbers
    remove_numbers = re.sub(r'\d+', '', text)
    # word tokenizing
    tonkenize_word = nltk.word_tokenize(remove_numbers)
    # remove_punctuations
    punt_removed = " ".join([w for w in tonkenize_word if w.lower() not in string.punctuation])
    # removing stopwords
    tokenize_punt_num_rem = nltk.word_tokenize(punt_removed)
    lang_stopwords = stopwords.words('english')
    stopwords_removed = " ".join([w for w in tokenize_punt_num_rem if w.lower() not in lang_stopwords])
    # stemming
    stem_words = []
    stemmer = SnowballStemmer('english')
    for word in nltk.word_tokenize(stopwords_removed):
        stem_words.append(stemmer.stem(word))

    stemmed_words = "".join(stem_words)

    n_grams = ngrams(stemmed_words, 3)
    tri_gram = [''.join(grams) for grams in n_grams]

    hash_value = [calc_hash(tri_gram[i], 11) for i in range(len(tri_gram))]

    arrLen = len(hash_value)
    prevMin = 0
    windows = []
    fingerprintList = []
    for i in range(arrLen - winSize):
        win = hash_value[i: i + winSize]  # forming windows
        windows.append(win)
        currMin = i + minIndex(win)
        if currMin != prevMin:
            fingerprintList.append(hash_value[currMin])
            prevMin = currMin
    return fingerprintList


# with open("hash_values.txt", 'r') as f:
#     data = json.loads(f.read())
#
# print(data['D:/Plagiarism Checker/plagiarismchecker/assignments/datasets/C Notes.pdf'])
