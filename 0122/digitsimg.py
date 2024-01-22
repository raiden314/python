from matplotlib import pyplot as plt
from PIL import Image
import numpy

path = "0122/2.png"
imgfile = Image.open(path).convert("L")
imgfile = imgfile.resize((8,8), Image.Resampling.LANCZOS)

data = numpy.asarray(imgfile,dtype=float)
print(data)


plt.imshow(data, cmap="grey")
plt.show()