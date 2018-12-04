import os
from collections import Counter
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score
import pickle

# Save to file
def save(clf, name):
    with open(name, 'wb') as fp:
        pickle.dump(clf, fp)
    print "saved"

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

# Prepare the dataset
def make_dataset(dictionary):
    direct = "/home/satej/PycharmProjects/SentenceClassifier/Email/data/"
    files = os.listdir(direct)

    emails = [direct + email for email in files]  # This list contains parts of file

    feature_set = []
    lables = []
    c = len(emails)

    for email in emails:
        data = []
        f = open(email)
        words = f.read().split(' ')
        for entry in dictionary:
            data.append(words.count(entry[0]))
        feature_set.append(data)

        if "ham" in email:
            lables.append(0)
        if "spam" in email:
            lables.append(1)
        print(c)
        c = c - 1
    return feature_set, lables

d = make_direct()
features, labels = make_dataset(d)
print(len(features), len(labels))

# Train and Test
x_train, x_test, y_train, y_test = tts(features, labels, test_size=0.2)

clf = MultinomialNB()
clf.fit(x_train, y_train)

preds= clf.predict(x_test)
print(accuracy_score(y_test, preds))
save(clf, "text-classifier.mdl")