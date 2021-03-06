# numpy
import numpy as np

# sklearn
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from sklearn.cluster import KMeans
from file_io import FileIO
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
import operator
import gensim
from gensim.models.keyedvectors import KeyedVectors

# load knn
print('loading knn')

stat = {}

with open('./datasets/word2vec_ag12bbc.txt', 'r', encoding='utf8') as f:
    lines = f.readlines()
    print(len(lines))
    labels = []
    features = []
    for line in lines:
        label = line.split('|sep|')[0]
        v = line.split('|sep|')[1].replace('\n', '').split(',')
        v = [float(i) for i in v]
        if label in stat.keys() and stat[label] < 5000:
            stat[label] += 1
            labels.append(label)
            features.append(v)
        elif label not in stat.keys():
            print(label)
            stat[label] = 1
            labels.append(label)
            features.append(v)
        else:
            pass
    f.close()

print(stat)

x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.3,
                                                    random_state=42)
classes = sorted(list(set(y_train)))
print(classes)
print('train', len(x_train))
print('test', len(x_test))
del labels
del features

neigh = KNeighborsClassifier(n_neighbors=50)
neigh.fit(x_train, y_train)

print('loading model')
# load google pretrained word2vec model
w2v_model = KeyedVectors.load_word2vec_format(
    './word2vec_model/GoogleNews-vectors-negative300.bin', binary=True)

from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords
import nltk.data
import operator, functools

# Load the punkt tokenizer
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
# English stop words
stops = set(stopwords.words("english"))


def get_deep_features(text):
    # Remove HTML
    text = BeautifulSoup(text).get_text()
    # Remove non-letters
    text = re.sub("[^a-zA-Z]", " ", text)
    # Convert words to lower case
    words = text.lower().split()
    words = [w for w in words if not w in stops]
    vectors = []
    print(words)
    for word in words:
        try:
            vectors.append(w2v_model[word])
        except Exception as e:
            # print(e)
            pass
    # print(len(vectors))
    if len(vectors) == 0:
        return []
    average_vector = functools.reduce(np.add, vectors)
    average_vector = average_vector / 300
    return average_vector


def get_labels(string, summary):
    sample = get_deep_features(string)
    if len(sample) == 0:
        return summary
    distances, neighbors = neigh.kneighbors(sample)
    neighbors = [y_train[n] for n in neighbors[0]]
    for n in neighbors:
        summary[n] += 1
    return summary

    # print('ready')

def result(file_name):
    with open('./fb_posts/' + file_name + '.txt', 'r', encoding='utf8') as fb_posts:
        summary = {}
        for c in classes:
            summary[c] = 0
        lines = fb_posts.readlines()
        count = 0
        for line in lines:
            summary = get_labels(line, summary)
            count += 1
            print(count)
        print(file_name)
        for s in sorted(summary.items(), key=operator.itemgetter(1), reverse=True):
            if s[1] != 0:
                print('\t', s[0], s[1])
