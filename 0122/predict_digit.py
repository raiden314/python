from sklearn import datasets, svm
from matplotlib import pyplot as plt
from PIL import Image
import numpy

digits = datasets.load_digits()

data_train = digits.data
label_train = digits.target

clf = svm.SVC(gamma=0.001)
clf.fit(data_train, label_train)



path = "0122/2.png"
imgfile = Image.open(path).convert("L")
imgfile = imgfile.resize((8,8), Image.Resampling.LANCZOS)
data = numpy.asarray(imgfile,dtype=float)
data = 16 - numpy.floor(17 * data / 256)

plt.imshow(data, cmap="Greys")
plt.show()

data = data.flatten()
print(data)

n = clf.predict([data])
print("予測数字＝",n)