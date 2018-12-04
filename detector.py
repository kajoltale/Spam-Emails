import pickle
import os
from sklearn import *
from collections import Counter

# Load
def load(clf_file):
    with open(clf_file) as fp:
        clf = pickle.load(fp)
    return clf

# Making a directory
def make_direct():
    direct = "/home/satej/PycharmProjects/SentenceClassifier/Email/data/"
    files = os.listdir(direct)

    emails = [direct + email for email in files]  # This list contains parts of file

    words = []
    c = len(emails)

    for email in emails:
        f = open(email)
        blob = f.read()
        words += blob.split(" ")
        print c
        c -= 1

    for i in range(len(words)):
        if not words[i].isalpha():
            words[i] = ""

    dictionary = Counter(words)
    del dictionary[""]  # Delete non alpha numeric words
    return dictionary.most_common(3000)

clf  = load("/home/satej/PycharmProjects/SentenceClassifier/Email/text-classifier.mdl")
d = make_direct()

while True:
    features = []
    inp = raw_input(">").split()
    if inp[0] == "exit":
        break
    for word in d:
        features.append(inp.count(word[0]))
    result = clf.predict([features])
    print ["Not spam", "Spam!"][result[0]]