from sklearn import datasets
from matplotlib import pyplot as plt

digits = datasets.load_digits()
idx=1500
print("答え＝",digits.target[idx])
data = digits.images[idx]

plt.imshow(data, cmap="Greys")
plt.show()