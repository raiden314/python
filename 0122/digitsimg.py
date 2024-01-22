from matplotlib import pyplot as plt
from PIL import Image

path = "0122/2.png"
imgfile = Image.open(path).convert("L")
imgfile = imgfile.resize((8,8))

data = imgfile


plt.imshow(data, cmap="grey")
plt.show()