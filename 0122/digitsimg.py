from matplotlib import pyplot as plt
from PIL import Image
import numpy

path = "0122/2.png"
imgfile = Image.open(path).convert("L")
imgfile = imgfile.resize((8,8), Image.Resampling.LANCZOS)
data = numpy.asarray(imgfile,dtype=float)
data = 16 - numpy.floor(17 * data / 256)
print(data)


plt.imshow(data, cmap="Greys")
plt.show()