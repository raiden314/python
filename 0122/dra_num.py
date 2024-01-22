from sklearn import datasets
from matplotlib import pyplot as plt

digits = datasets.load_digits()
data = digits.images[0]

plt.imshow(data, cmap="Greys")
plt.show()