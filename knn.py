from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans

with open('./datasets/7blkup_2_dfeatures.txt', 'r', encoding='utf8') as f:
    lines = f.readlines()
    labels = []
    features = []
    for line in lines:
        labels.append(line.split('|sep|')[0])
        features.append(line.split('|sep|')[1].split(','))
    print(labels[:10])
    print(len(features[0]))
    f.close()

x_train = features[:5000]
x_test = features
y_train = labels[:5000]
y_test = labels
# x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)
classes = sorted(list(set(y_train)))
print(classes)
print('train', len(x_train))
print('test', len(x_test))
del labels
del features

neigh = KNeighborsClassifier(n_neighbors=10)
neigh.fit(x_train, y_train)

predictions = []
count = len(x_test)
for sample in x_test:
    predictions.append(neigh.predict(sample))
    count = count - 1
    print(count)
print(predictions[:10])

t = 0
t_by_class = {}
total_by_class = {}
for i in range(len(predictions)):
    p = predictions[i][0]
    if p in total_by_class.keys():
        total_by_class[p] += 1
    else:
        total_by_class[p] = 1
    if p == y_test[i]:
        t += 1
        if p in t_by_class.keys():
            t_by_class[p] += 1
        else:
            t_by_class[p] = 1

print(t / len(predictions))
print()
print('knn train data,', len(x_train))
print('testing data', len(x_test))
for k in list(t_by_class.keys()):
    print(k, t_by_class[k] / total_by_class[k])
