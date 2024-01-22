from sklearn import datasets, svm
from sklearn.model_selection import train_test_split

digits = datasets.load_digits()

#訓練用とテスト用を用意 データと答えを準備
data_train, data_test, label_train, label_test = train_test_split(digits.data, digits.target)

print(len(data_train))
print(len(data_test))
print(len(label_train))
print(len(label_test))

clf = svm.SVC()
clf.fit(data_train, label_train)

