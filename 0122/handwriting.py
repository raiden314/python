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

predict = clf.predict( data_test )
#学習結果が正しいか、答え合わせする 左が導き出した答え、右が正しい答え
result = list(predict == label_test).count(True) / len(label_test)
print("正解率＝",result)