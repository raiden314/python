from matplotlib import pyplot as plt
import PIL.Image

path = "0122/2.png"
imgfile = PIL.Image.open(path).convert("L")

data = imgfile


plt.imshow(data, cmap="grey")
plt.show()